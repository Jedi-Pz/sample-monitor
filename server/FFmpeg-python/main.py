import ffmpeg
import threading
from screeninfo import get_monitors

monitors = get_monitors()

'''
if len(monitors) > 1:
    secondary_monitor = monitors[1]
    screen_x = secondary_monitor.width
    screen_y = secondary_monitor.height
else:
    raise Exception("No secondary monitor found.")
'''

secondary_monitor = monitors[0]
screen_x = secondary_monitor.width
screen_y = secondary_monitor.height

# 设置UDP传输地址和端口
udp_url = 'udp://127.0.0.1:12345'

'''
# 创建输出格式
output_format = 'mp4'
output_file = f'output.{output_format}'

netstat -ano | findstr :udp://127.0.0.1:1234

'''

input_params = {
    'f': 'gdigrab',
    'framerate': 30,
    'offset_x': monitors[0].x,
    'offset_y': monitors[0].y,
    's': f'{screen_x}x{screen_y}'
}

output_params = {
    'f': 'mp4',
    'vcodec': 'libx264',
    'pix_fmt': 'yuv420p',
    'vf': 'fps=30',
    's': '1920x1080',  # 根据需要调整分辨率
    # 'pkt_size': 1316
}

input_stream = ffmpeg.input('desktop', **input_params)
#output_stream = ffmpeg.output(input_stream, output_file, **output_params)
output_stream = ffmpeg.output(input_stream, udp_url, **output_params)


# 定时器回调函数
def stop_recording():
    process.communicate()  # 停止录制
    print("录制结束")

'''
# 设置录制时间（以秒为单位）
record_time = 10
timer = threading.Timer(record_time, stop_recording)
timer.start()
'''

# 开始录制
key1 = input("按 'q' 开始录制...")
if key1 == "q":
    # process = ffmpeg.run_async(output_stream)
    process = ffmpeg.run_async(output_stream)
    print("开始录制...")

# 结束录制
key2 = input("按 'q' 停止录制...")
if key2 == "q":
    #timer.cancel()  # 取消定时器
    process.terminate()  # 终止录制进程
    print("录制终止")
