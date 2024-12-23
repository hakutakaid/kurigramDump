#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class InputBusinessBotRecipients(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputBusinessBotRecipients`.

    Details:
        - Layer: ``195``
        - ID: ``C4E5921E``

    Parameters:
        existing_chats (``bool``, *optional*):
            N/A

        new_chats (``bool``, *optional*):
            N/A

        contacts (``bool``, *optional*):
            N/A

        non_contacts (``bool``, *optional*):
            N/A

        exclude_selected (``bool``, *optional*):
            N/A

        users (List of :obj:`InputUser <pyrogram.raw.base.InputUser>`, *optional*):
            N/A

        exclude_users (List of :obj:`InputUser <pyrogram.raw.base.InputUser>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["existing_chats", "new_chats", "contacts", "non_contacts", "exclude_selected", "users", "exclude_users"]

    ID = 0xc4e5921e
    QUALNAME = "types.InputBusinessBotRecipients"

    def __init__(self, *, existing_chats: Optional[bool] = None, new_chats: Optional[bool] = None, contacts: Optional[bool] = None, non_contacts: Optional[bool] = None, exclude_selected: Optional[bool] = None, users: Optional[List["raw.base.InputUser"]] = None, exclude_users: Optional[List["raw.base.InputUser"]] = None) -> None:
        self.existing_chats = existing_chats  # flags.0?true
        self.new_chats = new_chats  # flags.1?true
        self.contacts = contacts  # flags.2?true
        self.non_contacts = non_contacts  # flags.3?true
        self.exclude_selected = exclude_selected  # flags.5?true
        self.users = users  # flags.4?Vector<InputUser>
        self.exclude_users = exclude_users  # flags.6?Vector<InputUser>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputBusinessBotRecipients":
        
        flags = Int.read(b)
        
        existing_chats = True if flags & (1 << 0) else False
        new_chats = True if flags & (1 << 1) else False
        contacts = True if flags & (1 << 2) else False
        non_contacts = True if flags & (1 << 3) else False
        exclude_selected = True if flags & (1 << 5) else False
        users = TLObject.read(b) if flags & (1 << 4) else []
        
        exclude_users = TLObject.read(b) if flags & (1 << 6) else []
        
        return InputBusinessBotRecipients(existing_chats=existing_chats, new_chats=new_chats, contacts=contacts, non_contacts=non_contacts, exclude_selected=exclude_selected, users=users, exclude_users=exclude_users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.existing_chats else 0
        flags |= (1 << 1) if self.new_chats else 0
        flags |= (1 << 2) if self.contacts else 0
        flags |= (1 << 3) if self.non_contacts else 0
        flags |= (1 << 5) if self.exclude_selected else 0
        flags |= (1 << 4) if self.users else 0
        flags |= (1 << 6) if self.exclude_users else 0
        b.write(Int(flags))
        
        if self.users is not None:
            b.write(Vector(self.users))
        
        if self.exclude_users is not None:
            b.write(Vector(self.exclude_users))
        
        return b.getvalue()
