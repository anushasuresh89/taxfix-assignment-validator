columns = ['received_at', 'timestamp', 'context_device_manufacturer', 'context_locale', 'context_network_wifi', 'id', 'anonymous_id', 'context_device_type', 'event', 'event_text', 'user_id', 'context_device_token', 'context_device_model', 'context_os_name', 'original_timestamp', 'context_network_carrier', 'sent_at', 'context_device_ad_tracking_enabled', 'context_app_version', 'context_traits_taxfix_language', 'context_library_version', 'context_library_name', 'context_timezone']

list_values = {
	'context_device_manufacturer': ['apple', 'samsung', 'xiomi', 'lg', 'sony', 'nokia', 'oppo', 'panasonic', 'oneplus'],
	'context_device_type': ['android', 'symbian', 'ios'],
	'context_os_name': ['android', 'symbian', 'ios'],
	'context_locale': ['de-DE', 'in-IN', 'ne-NE', 'ic-IC', 'nr-NR', 'sw-SW', 'sz-SZ', 'fr-FR', 'it-IT', 'sp-SP'],
	'context_timezone': ['Europe/Berlin', 'Asia/Calcutta', 'Europe/London', 'Europe/Geneva'],
	'event': ['submission_success', 'registration_initiated'],
	'context_network_carrier': ['o2-de', 'vodafone', '1&1'],
	'context_traits_taxfix_language': ['de-DE', 'en-EN', 'de-SW', 'en-US', 'en-DE'],
	"context_library_name":[ "analytics-ios"],
	"event_text": ["submissionSuccess", "registrationInitiated"]
}

patterns = {
	'id': '[A-Z0-9]{8}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{12}',
	'anonymous_id': '[A-Z0-9]{8}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{12}',
	'context_app_version': '([0-9].){2}[0-9]',
	'context_library_version': '([0-9].){2}[0-9]',
	'context_device_model': 'iPhone|Galaxy|Nord',
}


nullables = ['context_device_manufacturer', 'context_locale', 'context_network_wifi', 'context_network_carrier', 'context_device_token', 'context_library_version', 'context_library_name']
