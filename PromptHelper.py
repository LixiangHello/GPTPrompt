import streamlit as st
import clipboard as pc

# 功能列表及其对应的prompt
func_prompts = {
    '英文学术润色': 'Below is a paragraph from an academic paper. '
                    'Polish the writing to meet the academic style, improve the '
                    'spelling, grammar, clarity, concision and overall readability. '
                    'When necessary, rewrite the whole sentence. Furthermore, list'
                    'all modification and explain the reasons to do so in markdown table.',

    '中文学术润色': '作为一名中文学术论文写作改进助理，你的任务是改进所提供文本的拼写、'
                    '语法、清晰、简洁和整体可读性，同时分解长句，减少重复，并提供改进建议。请只提供文本'
                    '的更正版本，避免包括解释。请编辑以下文本',
    '英文语法检查': 'Can you help me ensure that the grammar and the spelling 、'
                    'is correct? Do not try to polish the text, if no mistake is 、'
                    'found, tell me that this paragraph is good. If you find grammar 、'
                    'or spelling mistakes, please list mistakes you find in a two-column、'
                    'markdown table, put the original text the first column, put the、'
                    'corrected text in the second column and highlight the key 、'
                    'words you fixed. Example: Paragraph: How is you? Do you knows 、'
                    'what is it?',
    '英译汉': '请翻译成中文：',
    '汉译英': 'Please translate following sentence to English:',
    '解释代码': '请解释以下代码:',
    '找图片': '我需要你找一张网络图片。使用Unsplash API(https://source.unsplash.'
              'com/960x640/?<英语关键词>)获取图片URL，然后请使用Markdown格式封装，并且不'
              '要有反斜线，不要用代码块。现在，请按以下描述给我发送图片：',
}


def main():
    st.set_page_config('Prompt生成转换小工具')
    st.sidebar.markdown('# Prompt生成转换小工具\n\n')

    func_name = st.sidebar.selectbox('选择功能',
                                     options=list(func_prompts)
                                     )
    pre_text = func_prompts[func_name]

    st.sidebar.button('Re-run')

    st.header(func_name)
    st.text('\n')

    input_text = st.text_input('请输入文本', placeholder='文本')

    text = pre_text + input_text if input_text else ''
    st.text_area('转换输出',
                 text,
                 placeholder='等待输入...',
                 height=12
                 )

    if input_text:
        try:
            pc.copy(text)
            st.success('已复制到剪贴板.')
        except Exception as e:
            st.warning('Failed to AutoCopy.Please copy above context manually.', icon='⚠️')
            st.error(e)

main()
