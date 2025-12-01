const checkVersion = async () => {
  try {
    // We append a timestamp to bypass the cache of version.json itself
    const response = await fetch(`./version.json?t=${new Date().getTime()}`);
    const data = await response.json();
    
    // Store local version in localStorage or a constant
    const localVersion = localStorage.getItem('app_version'); 
    
    if (localVersion && localVersion !== data.version) {
      // Version mismatch detected!
      if (confirm('New version available. Reload?')) {
        // Update local version and reload
        localStorage.setItem('app_version', data.version);
        window.location.reload(true); // Force reload
      }
    } else if (!localVersion) {
       // First load
       localStorage.setItem('app_version', data.version);
    }
  } catch (err) {
    console.error('Failed to check version', err);
  }
};

// Check every 5 minutes
setInterval(checkVersion, 5 * 60 * 1000);
