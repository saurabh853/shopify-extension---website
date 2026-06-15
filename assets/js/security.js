// Trusted Types Policy Configuration
if (window.trustedTypes && window.trustedTypes.createPolicy) {
  if (!window.trustedTypes.defaultPolicy) {
    window.trustedTypes.createPolicy('default', {
      createHTML: (string) => string,
      createScript: (string) => string,
      createScriptURL: (url) => {
        try {
          const parsed = new URL(url, window.location.origin);
          if (
            parsed.origin === window.location.origin ||
            parsed.origin === 'https://www.googletagmanager.com' ||
            parsed.origin === 'https://www.google-analytics.com'
          ) {
            return url;
          }
        } catch (e) {
          if (url.startsWith('/') || !url.includes('://')) {
            return url;
          }
        }
        console.warn('Blocked untrusted script URL by Trusted Types:', url);
        return '';
      }
    });
  }
}

// Frame-busting clickjacking mitigation fallback
if (self !== top) {
  try {
    if (top.location.host !== self.location.host) {
      top.location = self.location;
    }
  } catch (e) {
    top.location = self.location;
  }
}
