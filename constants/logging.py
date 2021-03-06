LOG_FORMATTER = '%(asctime)s / %(name)s / %(levelname)s\n'\
        '| FILE: %(filename)s FUNCTION: %(funcName)s LINE: %(lineno)d |\nMESSAGE: %(message)s'

BOT_LOG_FILE = "logs/bot.log"

DB_CONNECTED = "Connected to DB"

BOT_START = "Starting bot"

GOOGLE_CALENDAR_CONNECTED = "Connected to Google Calendar"

GOOGLE_CALENDAR_EVENT_CREATED = "Event {0} added to the calendar"

INVALID_USER_STATE = "Invalid user state: {0}"

CALLBACK_QUERY_ERROR = "Callback query error"

COMMAND_START = "User: <{0}> fired start command"

DB_USER_ADDED = "User <{0}> with id <{1}> added to the database"

DB_USER_UPDATED = "User <{0}> with id <{1}> updated in the database"

DB_USER_DELETED = "User <{0}> with id <{1}> deleted from the database"

DB_USER_NOT_FOUND = "User with id <{0}> not found"

DB_USER_NOT_FOUND_BY_CHAT_ID = "User with chat_id <{0}> not found"

DB_EVENT_ADDED = "Event <{0}> with id <{1}> added to the database"

DB_EVENT_UPDATED = "Event <{0}> with id <{1}> updated in the database"

DB_EVENT_NOT_FOUND = "Event with id <{0}> not found"

EVENT_NO_ONGOING = "User <{0}> with id <{1}> event list: no ongoing events returned from DB"

EVENT_ONGOING = "User <{0}> with id <{1}> event list: return {2} events"

EVENT_NOTIFY = "User <{0}> with id <{1}> notified about event <{2}>"

EVENT_GOING = "User <{0}> with id <{1}> is going to event <{2}>"

EVENT_NOT_GOING = "User <{0}> with id <{1}> is not going to event <{2}>"

EVENT_DISABLED = "User <{0}> with id <{1}> disabled event <{2}>"

EVENT_ENABLED = "User <{0}> with id <{1}> enabled event <{2}>"

LOCATION_RECEIVED = "User <{0}> with id <{1}> has shared their location"

NO_ORGANIZER_FOR_EVENT = "No organizer record for event <{0}> with id <{1}>"

NO_ORGANIZER_LOCATION = "No location record for event <{0}> with id <{1}> organizer <{2}> with id <{3}>"

NEW_MEMBER_NOTIFIED = "Notified all users about new member <{0}> with id <{1}>"

BOT_BLOCKED = "User <{0}> with id <{1}> blocked the bot"

SM_INVITATION = "User <{0}> with id <{1}> invited user {2} with id {3} to the mafia"

SM_NEW_MEMBER = "User <{0}> with id <{1}> accepted the secret mafia invitation"

SM_DECLINED = "User <{0}> with id <{1}> declined the secret mafia invitation"

SM_NICKNAME_SET = "User <{0}> with id <{1}> chose nickname {2} for the SRM"

SM_NEW_MEMBER_NOTIFIED = "All SRM members notified about new member <{0}>"

USER_NAME_UPDATED = "Update name of user <{0}> with id <{1}> to {2} {3}"

SM_CHAT_NEW_MESSAGE = "User <{0}> with id <{1}> sent new message to the SRM chat"

USER_REMOVE_EXCEPTION = "Exception: {0} when removing a user with id {1}"

NEW_ANNOUNCEMENT = "User <{0}> with id <{1}> sent a new announcement <{2}>"