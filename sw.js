const CACHE_NAME = 'palabras-random-v2';
const urlsToCache = [
    './',
    './index.html',
    './app.js',
    './checkversion.js',
    './manifest.json',
    './icons/icon-72x72.png',
    './icons/icon-96x96.png',
    './icons/icon-128x128.png',
    './icons/icon-144x144.png',
    './icons/icon-152x152.png',
    './icons/icon-192x192.png',
    './icons/icon-384x384.png',
    './icons/icon-512x512.png'
];

// Helper function to check if URL is valid for caching
function isValidUrl(url) {
    return url.startsWith('http') || url.startsWith('https') || url.startsWith('./') || url.startsWith('/');
}

// Install event
self.addEventListener('install', (event) => {
    console.log('[ServiceWorker] Install');
    // Force the waiting service worker to become the active service worker
    self.skipWaiting();
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then((cache) => {
                console.log('[ServiceWorker] Caching app shell');
                return cache.addAll(urlsToCache);
            })
    );
});

// Activate event
self.addEventListener('activate', (event) => {
    console.log('[ServiceWorker] Activate');
    event.waitUntil(
        caches.keys().then((keyList) => {
            return Promise.all(keyList.map((key) => {
                if (key !== CACHE_NAME) {
                    console.log('[ServiceWorker] Removing old cache', key);
                    return caches.delete(key);
                }
            }));
        })
    );
    return self.clients.claim();
});

// Fetch event
self.addEventListener('fetch', (event) => {
    if (!isValidUrl(event.request.url)) {
        console.log('[ServiceWorker] Skipping invalid URL:', event.request.url);
        return;
    }
    
    // Network-Only strategy for version.json
    // We never want to serve this from cache, or cache the result.
    if (event.request.url.includes('version.json')) {
        event.respondWith(
            fetch(event.request).catch(() => {
                // Optional: If offline, you can return a fallback or nothing
                return new Response(JSON.stringify({ version: 'offline' }));
            })
        );
        return;
    }
    
    // Standard Cache-First strategy for everything else
    event.respondWith(
        caches.match(event.request)
            .then((response) => {
                if (response) {
                    console.log('[ServiceWorker] Found in cache:', event.request.url);
                    return response;
                }

                return fetch(event.request)
                    .then((response) => {
                        // Check if we received a valid response
                        if (!response || response.status !== 200 || response.type !== 'basic') {
                            return response;
                        }

                        // Clone the response
                        const responseToCache = response.clone();

                        caches.open(CACHE_NAME)
                            .then((cache) => {
                                console.log('[ServiceWorker] Caching new resource:', event.request.url);
                                cache.put(event.request, responseToCache);
                            });

                        return response;
                    })
                    .catch((error) => {
                        console.log('[ServiceWorker] Fetch failed:', error);
                        // You might want to return a custom offline page here
                    });
            })
    );
}); 
