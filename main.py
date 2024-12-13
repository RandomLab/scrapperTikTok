import pyktok as pyk
pyk.specify_browser('chrome')

pyk.save_tiktok('https://www.tiktok.com/@franceinfo/video/7442755346147429665',
	        True,
                'video_data.csv',
		'chrome')