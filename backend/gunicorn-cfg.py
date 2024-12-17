bind = '0.0.0.0:8000'  # Use port 8000 (or any other as needed)
workers = 3             # Adjust based on server capacity (could be dynamic based on CPU cores)
accesslog = '-'         # Stream access logs to stdout
loglevel = 'info'       # 'info' might be more suitable for production
capture_output = True   # Capture stdout and stderr
enable_stdio_inheritance = True  # Inherit parent process logs
timeout = 120           # Adjust timeout to a reasonable value (e.g., 120 seconds)

