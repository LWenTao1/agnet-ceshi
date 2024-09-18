# 导入必要的库
import openai
import os

# 配置 OpenAI API 密钥（请从环境变量中读取）
api_key = os.getenv("sk-zP6Fcai1LqMpXpOtZIjV5yW7EP7rUzJfgYv3mb-2kFT3BlbkFJ6LJRv9csS-3oYMLQhxxX1i8LSab3VvWxUHH8Y8cfkAY")  # 确保你使用有效的 OpenAI API 密钥
if not api_key:
    print("API 密钥未配置！请确保已设置环境变量 'YOUR_API_KEY'。")
else:
    openai.api_key = api_key

# 使用 GPT-4 解析古诗词的函数
def parse_poem_with_gpt4(poem_text):
    print("开始使用 GPT-4 解析诗词...")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # 使用 GPT-4 模型
            messages=[{"role": "user", "content": f"请解析以下诗词: {poem_text}"}],
            max_tokens=100
        )
        description = response['choices'][0]['message']['content'].strip()
        print(f"解析结果: {description}")
        return description
    except openai.error.OpenAIError as e:
        print(f"调用 OpenAI API 时发生错误: {e}")
        return None
    except Exception as e:
        print(f"未知错误: {e}")
        return None

# 定义一个生成图像描述的函数
def generate_image_prompt(description):
    print(f"生成图像描述的提示词: {description}")
    return f"根据以下描述生成图像：{description}"

# 定义一个生成图像的函数
def generate_image(description):
    print("调用 OpenAI API 生成图像...")
    try:
        response = openai.Image.create(
            prompt=description,  # 提供给 API 的提示词
            n=1,  # 生成的图像数量
            size="1024x1024"  # 图像的尺寸
        )
        image_url = response['data'][0]['url']  # 从响应中提取生成的图像 URL
        print(f"图像生成成功！URL: {image_url}")
        return image_url  # 返回生成的图像 URL
    except openai.error.OpenAIError as e:
        print(f"图像生成时发生错误: {e}")
        return None
    except Exception as e:
        print(f"未知错误: {e}")
        return None

# 测试代码块
print("开始测试 GPT-4 模型解析和图像生成...")

try:
    # 输入示例古诗词文本
    poem_text = "朝辞白帝彩云间，千里江陵一日还，两岸猿声啼不住，轻舟已过万重山。"

    # 使用 GPT-4 解析诗词
    description = parse_poem_with_gpt4(poem_text)
    
    if description:
        # 根据解析生成图像描述的提示词
        image_prompt = generate_image_prompt(description)
        
        # 调用 OpenAI API 生成图像
        image_url = generate_image(image_prompt)
        
        print(f"生成的图像URL: {image_url}")
    else:
        print("诗词解析失败，无法生成图像。")

except Exception as e:
    print(f"在处理诗词和生成图像时发生错误: {e}")