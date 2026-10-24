// Deployment config. These two values are PUBLIC by design (the anon key is safe in a browser because row level
// security protects the data). NEVER put the service_role key, Stripe secret key or Stripe webhook secret here.
window.MI_CONFIG = {
  SUPABASE_URL: 'SUPABASE_URL',        // e.g. https://abcdxyz.supabase.co
  ANON_KEY: 'ANON_KEY',                // Supabase > Project Settings > API > anon public
  PAYMENT_MODE: 'paynow_manual',       // 'paynow_manual' during the beta (default, also the fallback), 'stripe' at launch
  PAYNOW_TO: 'PayNow number or UEN (to confirm)',  // shown to parents with their reference code
  SITE_NAME: 'Math Inquirers'
};
