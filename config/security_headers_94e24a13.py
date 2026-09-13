# SAFE: Strict Security Headers & Error Masking
SECURE_HEADERS = {
    'X-Content-Type-Options': 'nosniff',
    'X-Frame-Options': 'DENY',
    'Content-Security-Policy': "default-src 'self'",
    'Server': 'CyberShield-Protected'
}