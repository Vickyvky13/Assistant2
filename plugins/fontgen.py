"""
• {i}fonts <font name> <text>
    Generate different fonts for the text.
"""

from . import _default, _double_stroke, _monospace, _small_caps

fonts = ["small caps ", "monospace ", "double stroke ", "script royal"]


@ultroid_cmd(
    pattern="font ?(.*)",
)
async def _(e):
    input = e.pattern_match.group(1)
    if not input:
        m = "**Available Fonts**\n\n"
        for x in fonts:
            m += f"• `{x}`\n"
        return await eod(e, m)
    try:
        font = input.split(":", maxsplit=1)[0]
        text = input.split(":", maxsplit=1)[1]
    except BaseException:
        return await eod(e, "`fonts small caps : chala jaa bsdk`")
    if font not in fonts:
        return await eod(e, f"`{font} not in font list`.")
    if font == "small caps ":
        msg = gen_font(text, _small_caps)
    if font == "monospace ":
        msg = gen_font(text, _monospace)
    if font == "double stroke ":
        msg = gen_font(text, _double_stroke)
    if font == "script royal ":
        msg = gen_font(text, _script_royal)
    await eor(e, msg)


def gen_font(text, new_font):
    for q in text:
        if q in _default:
            new = new_font[_default.index(q)]
            text = text.replace(q, new)
    return text
