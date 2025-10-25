#!/usr/bin/env python3
import time
import random
import sys
from datetime import datetime

def print_slowly(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def clear_screen():
    print("\n" * 2)

def print_heart():
    heart = """
    ♥♥♥♥♥♥♥     ♥♥♥♥♥♥♥
  ♥♥♥♥♥♥♥♥♥   ♥♥♥♥♥♥♥♥♥
 ♥♥♥♥♥♥♥♥♥♥♥ ♥♥♥♥♥♥♥♥♥♥♥
 ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
 ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
  ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
   ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
    ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
      ♥♥♥♥♥♥♥♥♥♥♥♥♥
        ♥♥♥♥♥♥♥♥♥
          ♥♥♥♥♥
            ♥
"""
    print("\033[91m" + heart + "\033[0m")

def print_stars():
    stars = """
    ✨ ⭐ ✨ ⭐ ✨ ⭐ ✨ ⭐ ✨ ⭐ ✨
    ⭐ ✨ ⭐ ✨ ⭐ ✨ ⭐ ✨ ⭐ ✨ ⭐
    ✨ ⭐ ✨ ⭐ ✨ ⭐ ✨ ⭐ ✨ ⭐ ✨
"""
    print("\033[93m" + stars + "\033[0m")

def get_sweet_messages():
    messages = [
        "你的笑容，是我见过最美的风景 🌸",
        "遇见你，是我这辈子最幸运的事 🍀",
        "每一天和你在一起，都是最好的一天 ☀️",
        "你就像星星一样，照亮了我的世界 ⭐",
        "在我心里，你永远是最特别的存在 💎",
        "因为有你，每个平凡的日子都变得闪闪发光 ✨",
        "你的存在，让这个世界变得温柔而美好 🌹",
        "和你在一起的时光，是我最珍贵的回忆 📸",
        "你是我的小太阳，温暖着我的每一天 🌞",
        "爱你，不是三分钟热度，而是久久的深情 💕"
    ]
    return messages

def show_romantic_journey():
    print_slowly("\n🗺️  让我为你规划一段浪漫的旅程...\n", 0.05)
    time.sleep(1)
    
    journeys = [
        {
            "theme": "🌸 春日约会",
            "places": ["樱花公园", "咖啡馆", "美术馆", "夕阳观景台"],
            "description": "在樱花飘落的季节，和你一起漫步"
        },
        {
            "theme": "🌙 星空之旅",
            "places": ["天文馆", "山顶观星点", "夜市小吃街", "江边散步道"],
            "description": "在星空下，与你分享每一个美好瞬间"
        },
        {
            "theme": "🎨 艺术探索",
            "places": ["艺术展览馆", "创意市集", "特色书店", "音乐餐厅"],
            "description": "在艺术的世界里，发现更多关于你的美好"
        },
        {
            "theme": "🍰 美食之旅",
            "places": ["网红甜品店", "特色餐厅", "私房烘焙坊", "茶室"],
            "description": "品尝美食的同时，品味和你在一起的甜蜜"
        }
    ]
    
    journey = random.choice(journeys)
    
    print_slowly(f"✨ {journey['theme']}", 0.05)
    print_slowly(f"   {journey['description']}\n", 0.04)
    time.sleep(0.5)
    
    print_slowly("🚗 行程安排:", 0.05)
    for i, place in enumerate(journey['places'], 1):
        time.sleep(0.3)
        print_slowly(f"   {i}. {place}", 0.04)
    
    print()

def show_love_quiz():
    print_slowly("\n💝 爱的小测试\n", 0.05)
    time.sleep(0.5)
    
    questions = [
        {
            "q": "如果用一种颜色形容你的心情，你会选择什么颜色？",
            "responses": {
                "红": "热情如火，就像你给我的温暖 ❤️",
                "蓝": "平静如水，你的温柔让我心安 💙",
                "粉": "浪漫甜蜜，和你在一起的每一刻 💗",
                "黄": "明亮欢快，你的笑容如同阳光 💛",
                "紫": "神秘优雅，你总是那么特别 💜"
            }
        },
        {
            "q": "最想和我一起做的事是什么？",
            "responses": {
                "旅行": "世界很大，我想和你一起去看看 ✈️",
                "看电影": "在黑暗的电影院，悄悄牵着你的手 🎬",
                "做饭": "为你做一顿爱心料理，是我的小幸福 🍳",
                "散步": "和你并肩走在夕阳下，就很美好 🌅",
                "聊天": "和你说话永远不会累，每句都是甜蜜 💬"
            }
        }
    ]
    
    question = random.choice(questions)
    print_slowly(f"❓ {question['q']}\n", 0.04)
    
    print("请选择：")
    options = list(question['responses'].keys())
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt}")
    
    try:
        choice = input("\n👉 你的选择 (1-5): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            selected = options[int(choice) - 1]
            print()
            print_slowly(f"💕 {question['responses'][selected]}", 0.04)
        else:
            print_slowly("\n💕 无论你选择什么，我都会一直陪着你", 0.04)
    except:
        print_slowly("\n💕 无论你选择什么，我都会一直陪着你", 0.04)

def show_music():
    music = """
    🎵 ♪ ♫ ♬ ♪ ♫ ♬ 🎵
    
    为你唱一首歌 🎤
    这首歌属于我们
    每个音符都是
    我对你的爱意
    
    ♪ ♫ ♬ ♪ ♫ ♬ ♪ ♫
"""
    print("\033[96m" + music + "\033[0m")

def show_countdown_of_love():
    print_slowly("\n⏰ 爱的时光机\n", 0.05)
    
    now = datetime.now()
    print_slowly(f"此刻: {now.strftime('%Y年%m月%d日 %H:%M:%S')}\n", 0.04)
    
    messages = [
        "从遇见你开始，每一秒都值得纪念 ⏱️",
        "时光荏苒，对你的爱却历久弥新 💝",
        "愿未来的每一天，都有你的陪伴 🌈"
    ]
    
    for msg in messages:
        time.sleep(0.5)
        print_slowly(f"  {msg}", 0.04)

def main():
    clear_screen()
    
    print("\033[95m" + "=" * 50 + "\033[0m")
    print_slowly("\n✨ 一个特别的惊喜，送给特别的你 ✨\n", 0.05)
    print("\033[95m" + "=" * 50 + "\033[0m")
    
    time.sleep(1)
    
    print_heart()
    time.sleep(1)
    
    print_stars()
    time.sleep(1)
    
    print_slowly("\n💌 今天想对你说...\n", 0.05)
    time.sleep(0.5)
    
    messages = get_sweet_messages()
    selected_messages = random.sample(messages, 3)
    
    for msg in selected_messages:
        time.sleep(0.8)
        print_slowly(f"  💝 {msg}", 0.04)
    
    time.sleep(1.5)
    
    show_romantic_journey()
    time.sleep(1.5)
    
    show_music()
    time.sleep(1)
    
    show_love_quiz()
    time.sleep(1)
    
    show_countdown_of_love()
    time.sleep(1)
    
    print("\n")
    print_stars()
    time.sleep(0.5)
    
    print_slowly("\n" + "=" * 50, 0.02)
    print_slowly("🌹 记住：无论何时，你都是最棒的！ 🌹", 0.05)
    print_slowly("💕 Love you forever and always 💕", 0.05)
    print_slowly("=" * 50 + "\n", 0.02)
    
    print_heart()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n💕 再见！爱你哦~ 💕\n")
        sys.exit(0)
