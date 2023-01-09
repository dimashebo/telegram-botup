from .base import StringConstant


class ApiMethod(StringConstant):
    pass


GET_UPDATES = ApiMethod('getUpdates')
SET_WEBHOOK = ApiMethod('setWebhook')
DELETE_WEBHOOK = ApiMethod('deleteWebhook')
GET_WEBHOOK_INFO = ApiMethod('getWebhookInfo')
GET_ME = ApiMethod('getMe')
LOGOUT = ApiMethod('logOut')
CLOSE = ApiMethod('close')
SEND_MESSAGE = ApiMethod('sendMessage')
FORWARD_MESSAGE = ApiMethod('forwardMessage')
COPY_MESSAGE = ApiMethod('copyMessage')
SEND_LOCATION = ApiMethod('sendLocation')
SEND_PHOTO = ApiMethod('sendPhoto')
SEND_AUDIO = ApiMethod('sendAudio')
SEND_DOCUMENT = ApiMethod('sendDocument')
SEND_VIDEO = ApiMethod('sendVideo')
SEND_ANIMATION = ApiMethod('sendAnimation')
SEND_VOICE = ApiMethod('sendVoice')
SEND_VIDEO_NOTE = ApiMethod('sendVideoNote')
SEND_MEDIA_GROUP = ApiMethod('sendMediaGroup')
EDIT_MESSAGE_LIVE_LOCATION = ApiMethod('editMessageLiveLocation')
STOP_MESSAGE_LIVE_LOCATION = ApiMethod('stopMessageLiveLocation')
SEND_VENUE = ApiMethod('sendVenue')
SEND_CONTACT = ApiMethod('sendContact')
SEND_POLL = ApiMethod('sendPoll')
SEND_DICE = ApiMethod('sendDice')
SEND_CHAT_ACTION = ApiMethod('sendChatAction')
GET_USER_PROFILE_PHOTOS = ApiMethod('getUserProfilePhotos')
GET_FILE = ApiMethod('getFile')
BAN_CHAT_MEMBER = ApiMethod('banChatMember')
UNBAN_CHAT_MEMBER = ApiMethod('unbanChatMember')
RESTRICT_CHAT_MEMBER = ApiMethod('restrictChatMember')
PROMOTE_CHAT_MEMBER = ApiMethod('promoteChatMember')
SET_CHAT_ADMINISTRATOR_CUSTOM_TITLE = ApiMethod('setChatAdministratorCustomTitle')
BAN_CHAT_SENDER_CHAT = ApiMethod('banChatSenderChat')
UNBAN_CHAT_SENDER_CHAT = ApiMethod('unbanChatSenderChat')
SET_CHAT_PERMISSIONS = ApiMethod('setChatPermissions')
EXPORT_CHAT_INVITE_LINK = ApiMethod('exportChatInviteLink')
CREATE_CHAT_INVITE_LINK = ApiMethod('createChatInviteLink')
EDIT_CHAT_INVITE_LINK = ApiMethod('editChatInviteLink')
REVOKE_CHAT_INVITE_LINK = ApiMethod('revokeChatInviteLink')
APPROVE_CHAT_JOIN_REQUEST = ApiMethod('approveChatJoinRequest')
DECLINE_CHAT_JOIN_REQUEST = ApiMethod('decline_chat_join_request')
SET_CHAT_PHOTO = ApiMethod('setChatPhoto')
DELETE_CHAT_PHOTO = ApiMethod('deleteChatPhoto')
SET_CHAT_TITLE = ApiMethod('setChatTitle')
SET_CHAT_DESCRIPTION = ApiMethod('setChatDescription')
PIN_CHAT_MESSAGE = ApiMethod('pinChatMessage')
UNPIN_CHAT_MESSAGE = ApiMethod('unpinChatMessage')
UNPIN_ALL_CHAT_MESSAGES = ApiMethod('unpinAllChatMessages')
LEAVE_CHAT = ApiMethod('leaveChat')
GET_CHAT = ApiMethod('getChat')
GET_CHAT_ADMINISTRATORS = ApiMethod('getChatAdministrators')
GET_CHAT_MEMBER_COUNT = ApiMethod('getChatMemberCount')
GET_CHAT_MEMBER = ApiMethod('getChatMember')
SET_CHAT_STICKER_SET = ApiMethod('setChatStickerSet')
DELETE_CHAT_STICKER_SET = ApiMethod('deleteChatStickerSet')
GET_FORUM_TOPIC_ICON_STICKERS = ApiMethod('getForumTopicIconStickers')
CREATE_FORUM_TOPIC = ApiMethod('createForumTopic')
EDIT_FORUM_TOPIC = ApiMethod('editForumTopic')
CLOSE_FORUM_TOPIC = ApiMethod('closeForumTopic')
REOPEN_FORUM_TOPIC = ApiMethod('reopenForumTopic')
DELETE_FORUM_TOPIC = ApiMethod('deleteForumTopic')
UNPIN_ALL_FORUM_TOPIC_MESSAGES = ApiMethod('unpinAllForumTopicMessages')
EDIT_GENERAL_FORUM_TOPIC = ApiMethod('editGeneralForumTopic')
CLOSE_GENERAL_FORUM_TOPIC = ApiMethod('closeGeneralForumTopic')
REOPEN_GENERAL_FORUM_TOPIC = ApiMethod('reopenGeneralForumTopic')
HIDE_GENERAL_FORUM_TOPIC = ApiMethod('hideGeneralForumTopic')
UNHIDE_GENERAL_FORUM_TOPIC = ApiMethod('unhideGeneralForumTopic')
ANSWER_CALLBACK_QUERY = ApiMethod('answerCallbackQuery')
SET_MY_COMMANDS = ApiMethod('setMyCommands')
DELETE_MY_COMMANDS = ApiMethod('deleteMyCommands')
GET_MY_COMMANDS = ApiMethod('getMyCommands')
SET_CHAT_MENU_BUTTON = ApiMethod('setChatMenuButton')
GET_CHAT_MENU_BUTTON = ApiMethod('getChatMenuButton')
SET_MY_DEFAULT_ADMINISTRATOR_RIGHTS = ApiMethod('setMyDefaultAdministratorRights')
GET_MY_DEFAULT_ADMINISTRATOR_RIGHTS = ApiMethod('getMyDefaultAdministratorRights')
EDIT_MESSAGE_TEXT = ApiMethod('editMessageText')
EDIT_MESSAGE_CAPTION = ApiMethod('editMessageCaption')
EDIT_MESSAGE_MEDIA = ApiMethod('editMessageMedia')
EDIT_MESSAGE_REPLY_MARKUP = ApiMethod('editMessageReplyMarkup')
STOP_POLL = ApiMethod('stopPoll')
DELETE_MESSAGE = ApiMethod('deleteMessage')
SEND_STICKER = ApiMethod('sendSticker')
GET_STICKER_SET = ApiMethod('getStickerSet')
GET_CUSTOM_EMOJI_STICKERS = ApiMethod('getCustomEmojiStickers')
UPLOAD_STICKER_FILE = ApiMethod('uploadStickerFile')
CREATE_NEW_STICKER_SET = ApiMethod('createNewStickerSet')
ADD_STICKER_TO_SET = ApiMethod('addStickerToSet')
SET_STICKER_POSITION_IN_SET = ApiMethod('setStickerPositionInSet')
DELETE_STICKER_FROM_SET = ApiMethod('deleteStickerFromSet')
SET_STICKER_SET_THUMB = ApiMethod('setStickerSetThumb')
ANSWER_INLINE_QUERY = ApiMethod('answerInlineQuery')
ANSWER_WEB_APP_QUERY = ApiMethod('answerWebAppQuery')
SEND_INVOICE = ApiMethod('sendInvoice')
CREATE_INVOICE_LINK = ApiMethod('createInvoiceLink')
ANSWER_SHIPPING_QUERY = ApiMethod('answerShippingQuery')
ANSWER_PRE_CHECKOUT_QUERY = ApiMethod('answerPreCheckoutQuery')
SET_PASSPORT_DATA_ERRORS = ApiMethod('setPassportDataErrors')
SEND_GAME = ApiMethod('sendGame')
SET_GAME_HIGH_SCORE = ApiMethod('setGameHighScore')
GET_GAME_HIGH_SCORES = ApiMethod('getGameHighScores')