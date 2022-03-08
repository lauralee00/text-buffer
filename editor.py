from define_tbuf import *
from utility_tbuf import *
from typing import *


class Editor:
    def __init__(self, row: Optional[int], col: Optional[int], buf: Optional[TextBuffer]):
        self.buf = buf
        self.row = row
        self.col = col

# implementation:

# A valid editor data structure is:
# - non-NULL
# - has a valid text buffer
# - has recorded row and col fields
# - that match tbuf_row() and tbuf_col()
def is_editor(editor: Editor) -> bool:
    if not editor:
        return False

    buf = editor.buf
    row, col = buf.row, buf.col

    return is_tbuf(buf) and tbuf_row(buf) == row and tbuf_col(buf) == col


# interface functions:

# Create a new and empty editor
def editor_new() -> Editor:
    # ENSURES: is_editor(\result)
    new = Editor(row=1, col=0, buf=tbuf_new())
    return new

# Move the cursor forward, to the right
def editor_forward(E: Editor) -> None:
    buf = E
    if buf.cursor != buf.end:
        tbuf_forward(buf)

# Move the cursor backward, to the left
def editor_backward(E: Editor) -> None:
    buf = E
    if buf.cursor != buf.start.next:
        tbuf_backward(buf)

# Insert c to the cursor’s left
def editor_insert(E: Editor, c: str) -> None:
    tbuf_insert(E, c)

# Remove the node to the cursor’s left
def editor_delete(E: Editor) -> None:
    buf = E
    if is_tbuf(buf) and not tbuf_is_empty(buf) and not buf.cursor.prev == buf.start:
        tbuf_delete(buf)


# TODO: implement editor_up() and editor_down()
# # moves cursor one line above
# # preserves original column unless new line has fewer columns
# #   in which case cursor is placed at the rightmost column
# def editor_up(E: Editor) -> None:
#     r, c = tbuf_row(B), tbuf_col(B)
#     if r == 1: #first line
#         return
#     while E.buf.cursor.data != "\n":
#         editor_forward(E)
#
#     newC = tbuf_col(B)
#     for i in range(c-newC):
#         editor_forward(E)
#         if E.buf.cursor.data == "\n":
#             break
#
#
# # moves cursor one line below
# # preserves original column unless new line has fewer columns
# #   in which case cursor is placed at the rightmost column
# def editor_down(E: Editor) -> None:
#     r, c = tbuf_row(E), tbuf_col(E)
#     if r == E.row:
#         return
#     while E.buf.cursor.data != "\n":
#         editor_backward(E)
#
#     for i in range(c):



