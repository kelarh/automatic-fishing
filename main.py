import pyautogui
import pygetwindow as gw
import time

# 窗口标题
window_title = "雷电模拟器"  # 替换为目标窗口的标题

# 获取窗口对象
window = gw.getWindowsWithTitle(window_title)
if not window:
    print("没有找到指定的窗口")
    exit()

target_window = window[0]
# 获取窗口的位置和尺寸
window_left = target_window.left
window_top = target_window.top
window_width = target_window.width
window_height = target_window.height

# 计算图标在窗口中的相对位置
Throwing_pole_x = window_left + 1625
Throwing_pole_y = window_top + 884
# 目标图像的路径
target_image = 'Retry.png'  # 替换为你的目标图像路径

def throw_pole():   
    pyautogui.click(Throwing_pole_x, Throwing_pole_y)
    pyautogui.dragRel(0, -300, duration=0.5)
    print("抛竿成功！")

    time.sleep(5.75)
    pyautogui.click(Throwing_pole_x, Throwing_pole_y)
    print("提竿成功！")

def click_and_check():
    # 连续快速点击的次数
    click_count = 50
    # 点击的间隔（秒）
    interval = 0.03  # 30ms间隔
    total_clicks = 0 # 总点击次数

    for i in range(click_count):

        pyautogui.click(Throwing_pole_x, Throwing_pole_y)  # 模拟点击
        total_clicks += 1  # 累加点击次数
        time.sleep(interval)  # 设置每次点击之间的间隔

        # 每 30 次点击后停顿 1 秒并检查图像
        if (i + 1) % 50 == 0:
            print(f"已点击 {total_clicks} 次，等待 1.4 秒，检查目标图像...")
            time.sleep(1.4)  # 停顿 1.4 秒

            # 检查图像是否出现在屏幕上
            try:
                target_location = pyautogui.locateOnScreen(target_image, confidence=0.8)

                if target_location:
                    print(f"目标图像已找到，进行点击！")
                    # 点击目标图像的中心位置
                    pyautogui.click(target_location)
                    return  # 图像已找到，退出函数
                else:
                    print("未找到目标图像，继续点击...")
            except pyautogui.ImageNotFoundException:
                print("图像检测异常，继续执行点击。")
    
    print("未找到目标图像，重新开始...")
    click_and_check()  # 递归调用，重新开始点击过程

for i in range(100):            
    throw_pole()
    click_and_check()
    time.sleep(5)
    print(f"第 {i+1} 条鱼...")



