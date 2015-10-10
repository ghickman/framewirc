########
# BASE #
########

# Registration
NICK = 'NICK'
PASS = 'PASS'
QUIT = 'QUIT'
USER = 'USER'  # Sent when registering a new user.

# Channel ops
INVITE = 'INVITE'
JOIN = 'JOIN'
KICK = 'KICK'
LIST = 'LIST'
MODE = 'MODE'
NAMES = 'NAMES'
PART = 'PART'
TOPIC = 'TOPIC'

# Server ops
ADMIN = 'ADMIN'
CONNECT = 'CONNECT'
INFO = 'INFO'
LINKS = 'LINKS'
OPER = 'OPER'
REHASH = 'REHASH'
RESTART = 'RESTART'
SERVER = 'SERVER'  # Sent when registering as a server.
SQUIT = 'SQUIT'
STATS = 'STATS'
SUMMON = 'SUMMON'
TIME = 'TIME'
TRACE = 'TRACE'
VERSION = 'VERSION'
WALLOPS = 'WALLOPS'

# Sending messages
NOTICE = 'NOTICE'
PRIVMSG = 'PRIVMSG'

# User queries
WHO = 'WHO'
WHOIS = 'WHOIS'
WHOWAS = 'WHOWAS'

# Misc
ERROR = 'ERROR'
KILL = 'KILL'
PING = 'PING'
PONG = 'PONG'

# Optional
AWAY = 'AWAY'
USERS = 'USERS'
USERHOST = 'USERHOST'
ISON = 'ISON'  # "Is on"

###########
# REPLIES #
###########

# 001 to 004 are sent to a user upon successful registration.
RPL_WELCOME = '001'
RPL_YOURHOST = '002'
RPL_CREATED = '003'
RPL_MYINFO = '004'

# Sent by the server to suggest an alternative server when full or refused.
RPL_BOUNCE = '005'

# Reply to the USERHOST command.
RPL_USERHOST = '302'

# Reply to the ISON command (to see if a user "is on").
RPL_ISON = '303'

# Sent to any client sending a PRIVMSG to a client which is away.
RPL_AWAY = '301'

# Acknowledgements of the AWAY command.
RPL_UNAWAY = '305'
RPL_NOWAWAY = '306'

# Replies to a WHOIS message.
RPL_WHOISUSER = '311'
RPL_WHOISSERVE = '312'
RPL_WHOISOPERATOR = '313'
RPL_WHOISIDLE = '317'
RPL_ENDOFWHOIS = '318'
RPL_WHOISCHANNELS = '319'

# Replies to WHOWAS command. See also ERR_WASNOSUCHNICK.
RPL_WHOWASUSER = '314'
RPL_ENDOFWHOWAS = '369'

# Replies to LIST command. Note that 321 is obsolete and unused.
RPL_LISTSTART = '321'
RPL_LIST = '322'
RPL_LISTEND = '323'

# Replies to MODE. I don't understand the spec of 325!
RPL_CHANNELMODEIS = '324'
RPL_UNIQOPIS = '325'
RPL_INVITELIST = '346'
RPL_ENDOFINVITELIST = '347'
RPL_EXCEPTLIST = '348'
RPL_ENDOFEXCEPTLIST = '349'
RPL_BANLIST = '367'
RPL_ENDOFBANLIST = '368'
RPL_UMODEIS = '221'

# Replies to TOPIC.
RPL_NOTOPIC = '331'
RPL_TOPIC = '332'

# Acknowledgement of INVITE command.
RPL_INVITING = '341'

# Acknowledgement of SUMMON command.
RPL_SUMMONING = '342'

# Reply to VERSION.
RPL_VERSION = '351'

# Reply to WHO.
RPL_WHOREPLY = '352'
RPL_ENDOFWHO = '315'

# Reply to NAMES.
RPL_NAMREPLY = '353'
RPL_ENDOFNAMES = '366'

# Reply to LINKS.
RPL_LINKS = '364'
RPL_ENDOFLINKS = '365'

# Reply to INFO.
RPL_INFO = '371'
RPL_ENDOFINFO = '374'

# Reply to MOTD. Also usually sent upon successful registration.
RPL_MOTDSTART = '375'
RPL_MOTD = '372'
RPL_ENDOFMOTD = '376'

# Acknowledgement of OPER.
RPL_YOUREOPER = '381'

# Acknowledgement of REHASH.
RPL_REHASHING = '382'

# Reply to SERVICE upon successful registration.
RPL_YOURESERVICE = '383'

# Reply to TIME.
RPL_TIME = '391'

# Replies to USERS.
RPL_USERSSTART = '392'
RPL_USERS = '393'
RPL_ENDOFUSERS = '394'
RPL_NOUSERS = '395'

# Replies to TRACE.
RPL_TRACELINK = '200'
RPL_TRACECONNECTING = '201'
RPL_TRACEHANDSHAKE = '202'
RPL_TRACEUNKNOWN = '203'
RPL_TRACEOPERATOR = '204'
RPL_TRACEUSER = '205'
RPL_TRACESERVER = '206'
RPL_TRACESERVICE = '207'
RPL_TRACENEWTYPE = '208'
RPL_TRACECLASS = '209'
RPL_TRACERECONNECT = '210'
RPL_TRACELOG = '261'
RPL_TRACEEND = '262'

# Reply to STATS. See also ERR_NOSUCHSERVER.
RPL_STATSLINKINFO = '211'
RPL_STATSCOMMANDS = '212'
RPL_ENDOFSTATS = '219'
RPL_STATSUPTIME = '242'
RPL_STATSOLINE = '243'

# Reply to SERVLIST.
RPL_SERVLIST = '234'
RPL_SERVLISTEND = '235'

# Reply to LUSERS.
RPL_LUSERCLIENT = '251'
RPL_LUSEROP = '252'
RPL_LUSERUNKNOWN = '253'
RPL_LUSERCHANNELS = '254'
RPL_LUSERME = '255'

# Reply to ADMIN.
RPL_ADMINME = '256'
RPL_ADMINLOC1 = '257'
RPL_ADMINLOC2 = '258'
RPL_ADMINEMAIL = '259'

# Sent when a server drops a command without processing it.
RPL_TRYAGAIN = '263'

##########
# ERRORS #
##########

ERR_NOSUCHNICK = '401'
ERR_NOSUCHSERVER = '402'
ERR_NOSUCHCHANNEL = '403'
ERR_CANNOTSENDTOCHAN = '404'
ERR_TOOMANYCHANNELS = '405'
ERR_WASNOSUCHNICK = '406'
ERR_TOOMANYTARGETS = '407'
ERR_NOSUCHSERVICE = '408'
ERR_NOORIGIN = '409'
ERR_NORECIPIENT = '411'
ERR_NOTEXTTOSEND = '412'
ERR_NOTOPLEVEL = '413'
ERR_WILDTOPLEVEL = '414'
ERR_BADMASK = '415'
ERR_UNKNOWNCOMMAND = '421'
ERR_NOMOTD = '422'
ERR_NOADMININFO = '423'
ERR_FILEERROR = '424'
ERR_NONICKNAMEGIVEN = '431'
ERR_ERRONEUSNICKNAME = '432'
ERR_NICKNAMEINUSE = '433'
ERR_NICKCOLLISION = '436'
ERR_UNAVAILRESOURCE = '437'
ERR_USERNOTINCHANNEL = '441'
ERR_NOTONCHANNEL = '442'
ERR_USERONCHANNEL = '443'
ERR_NOLOGIN = '444'
ERR_SUMMONDISABLED = '445'
ERR_USERSDISABLED = '446'
ERR_NOTREGISTERED = '451'
ERR_NEEDMOREPARAMS = '461'
ERR_ALREADYREGISTRED = '462'
ERR_NOPERMFORHOST = '463'
ERR_PASSWDMISMATCH = '464'
ERR_YOUREBANNEDCREEP = '465'
ERR_YOUWILLBEBANNED = '466'
ERR_KEYSET = '467'
ERR_CHANNELISFULL = '471'
ERR_UNKNOWNMODE = '472'
ERR_INVITEONLYCHAN = '473'
ERR_BANNEDFROMCHAN = '474'
ERR_BADCHANNELKEY = '475'
ERR_BADCHANMASK = '476'
ERR_NOCHANMODES = '477'
ERR_BANLISTFULL = '478'
ERR_NOPRIVILEGES = '481'
ERR_CHANOPRIVSNEEDED = '482'
ERR_CANTKILLSERVER = '483'
ERR_RESTRICTED = '484'
ERR_UNIQOPPRIVSNEEDED = '485'
ERR_NOOPERHOST = '491'
ERR_UMODEUNKNOWNFLAG = '501'
ERR_USERSDONTMATCH = '502'


#########
# Other #
#########

# Found in responses from freenode
# Names from https://www.alien.net.au/irc/irc2numerics.html
# Could not find in a spec.
RPL_STATSCONN = '250'
RPL_LOCALUSERS = '265'
RPL_GLOBALUSERS = '266'
RPL_CHANNEL_URL = '328'