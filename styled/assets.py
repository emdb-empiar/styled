# -*- coding: utf-8 -*-

ESC = u'\033'

END = u'{}[0m'.format(ESC)

STYLE_NAMES = {
    u'bold': u"1",
    u'dim': u"2",
    u'underlined': u"4",
    u'blink': u"5",
    u'reverse': u"7",
    u'hidden': u"8",
    u'reset': u"0",
    u'res_bold': u"21",
    u'res_dim': u"22",
    u'res_underlined': u"24",
    u'res_blink': u"25",
    u'res_reverse': u"27",
    u'res_hidden': u"28"
}

COLOURS = {
    u"black": u"0",
    u"red": u"1",
    u"green": u"2",
    u"yellow": u"3",
    u"blue": u"4",
    u"magenta": u"5",
    u"cyan": u"6",
    u"light_gray": u"7",
    u"dark_gray": u"8",
    u"light_red": u"9",
    u"light_green": u"10",
    u"light_yellow": u"11",
    u"light_blue": u"12",
    u"light_magenta": u"13",
    u"light_cyan": u"14",
    u"white": u"15",
    u"grey_0": u"16",
    u"navy_blue": u"17",
    u"dark_blue": u"18",
    u"blue_3a": u"19",
    u"blue_3b": u"20",
    u"blue_1": u"21",
    u"dark_green": u"22",
    u"deep_sky_blue_4a": u"23",
    u"deep_sky_blue_4b": u"24",
    u"deep_sky_blue_4c": u"25",
    u"dodger_blue_3": u"26",
    u"dodger_blue_2": u"27",
    u"green_4": u"28",
    u"spring_green_4": u"29",
    u"turquoise_4": u"30",
    u"deep_sky_blue_3a": u"31",
    u"deep_sky_blue_3b": u"32",
    u"dodger_blue_1": u"33",
    u"green_3a": u"34",
    u"spring_green_3a": u"35",
    u"dark_cyan": u"36",
    u"light_sea_green": u"37",
    u"deep_sky_blue_2": u"38",
    u"deep_sky_blue_1": u"39",
    u"green_3b": u"40",
    u"spring_green_3b": u"41",
    u"spring_green_2a": u"42",
    u"cyan_3": u"43",
    u"dark_turquoise": u"44",
    u"turquoise_2": u"45",
    u"green_1": u"46",
    u"spring_green_2b": u"47",
    u"spring_green_1": u"48",
    u"medium_spring_green": u"49",
    u"cyan_2": u"50",
    u"cyan_1": u"51",
    u"dark_red_1": u"52",
    u"deep_pink_4a": u"53",
    u"purple_4a": u"54",
    u"purple_4b": u"55",
    u"purple_3": u"56",
    u"blue_violet": u"57",
    u"orange_4a": u"58",
    u"grey_37": u"59",
    u"medium_purple_4": u"60",
    u"slate_blue_3a": u"61",
    u"slate_blue_3b": u"62",
    u"royal_blue_1": u"63",
    u"chartreuse_4": u"64",
    u"dark_sea_green_4a": u"65",
    u"pale_turquoise_4": u"66",
    u"steel_blue": u"67",
    u"steel_blue_3": u"68",
    u"cornflower_blue": u"69",
    u"chartreuse_3a": u"70",
    u"dark_sea_green_4b": u"71",
    u"cadet_blue_2": u"72",
    u"cadet_blue_1": u"73",
    u"sky_blue_3": u"74",
    u"steel_blue_1a": u"75",
    u"chartreuse_3b": u"76",
    u"pale_green_3a": u"77",
    u"sea_green_3": u"78",
    u"aquamarine_3": u"79",
    u"medium_turquoise": u"80",
    u"steel_blue_1b": u"81",
    u"chartreuse_2a": u"82",
    u"sea_green_2": u"83",
    u"sea_green_1a": u"84",
    u"sea_green_1b": u"85",
    u"aquamarine_1a": u"86",
    u"dark_slate_gray_2": u"87",
    u"dark_red_2": u"88",
    u"deep_pink_4b": u"89",
    u"dark_magenta_1": u"90",
    u"dark_magenta_2": u"91",
    u"dark_violet_1a": u"92",
    u"purple_1a": u"93",
    u"orange_4b": u"94",
    u"light_pink_4": u"95",
    u"plum_4": u"96",
    u"medium_purple_3a": u"97",
    u"medium_purple_3b": u"98",
    u"slate_blue_1": u"99",
    u"yellow_4a": u"100",
    u"wheat_4": u"101",
    u"grey_53": u"102",
    u"light_slate_grey": u"103",
    u"medium_purple": u"104",
    u"light_slate_blue": u"105",
    u"yellow_4b": u"106",
    u"dark_olive_green_3a": u"107",
    u"dark_green_sea": u"108",
    u"light_sky_blue_3a": u"109",
    u"light_sky_blue_3b": u"110",
    u"sky_blue_2": u"111",
    u"chartreuse_2b": u"112",
    u"dark_olive_green_3b": u"113",
    u"pale_green_3b": u"114",
    u"dark_sea_green_3a": u"115",
    u"dark_slate_gray_3": u"116",
    u"sky_blue_1": u"117",
    u"chartreuse_1": u"118",
    u"light_green_2": u"119",
    u"light_green_3": u"120",
    u"pale_green_1a": u"121",
    u"aquamarine_1b": u"122",
    u"dark_slate_gray_1": u"123",
    u"red_3a": u"124",
    u"deep_pink_4c": u"125",
    u"medium_violet_red": u"126",
    u"magenta_3a": u"127",
    u"dark_violet_1b": u"128",
    u"purple_1b": u"129",
    u"dark_orange_3a": u"130",
    u"indian_red_1a": u"131",
    u"hot_pink_3a": u"132",
    u"medium_orchid_3": u"133",
    u"medium_orchid": u"134",
    u"medium_purple_2a": u"135",
    u"dark_goldenrod": u"136",
    u"light_salmon_3a": u"137",
    u"rosy_brown": u"138",
    u"grey_63": u"139",
    u"medium_purple_2b": u"140",
    u"medium_purple_1": u"141",
    u"gold_3a": u"142",
    u"dark_khaki": u"143",
    u"navajo_white_3": u"144",
    u"grey_69": u"145",
    u"light_steel_blue_3": u"146",
    u"light_steel_blue": u"147",
    u"yellow_3a": u"148",
    u"dark_olive_green_3": u"149",
    u"dark_sea_green_3b": u"150",
    u"dark_sea_green_2": u"151",
    u"light_cyan_3": u"152",
    u"light_sky_blue_1": u"153",
    u"green_yellow": u"154",
    u"dark_olive_green_2": u"155",
    u"pale_green_1b": u"156",
    u"dark_sea_green_5b": u"157",
    u"dark_sea_green_5a": u"158",
    u"pale_turquoise_1": u"159",
    u"red_3b": u"160",
    u"deep_pink_3a": u"161",
    u"deep_pink_3b": u"162",
    u"magenta_3b": u"163",
    u"magenta_3c": u"164",
    u"magenta_2a": u"165",
    u"dark_orange_3b": u"166",
    u"indian_red_1b": u"167",
    u"hot_pink_3b": u"168",
    u"hot_pink_2": u"169",
    u"orchid": u"170",
    u"medium_orchid_1a": u"171",
    u"orange_3": u"172",
    u"light_salmon_3b": u"173",
    u"light_pink_3": u"174",
    u"pink_3": u"175",
    u"plum_3": u"176",
    u"violet": u"177",
    u"gold_3b": u"178",
    u"light_goldenrod_3": u"179",
    u"tan": u"180",
    u"misty_rose_3": u"181",
    u"thistle_3": u"182",
    u"plum_2": u"183",
    u"yellow_3b": u"184",
    u"khaki_3": u"185",
    u"light_goldenrod_2a": u"186",
    u"light_yellow_3": u"187",
    u"grey_84": u"188",
    u"light_steel_blue_1": u"189",
    u"yellow_2": u"190",
    u"dark_olive_green_1a": u"191",
    u"dark_olive_green_1b": u"192",
    u"dark_sea_green_1": u"193",
    u"honeydew_2": u"194",
    u"light_cyan_1": u"195",
    u"red_1": u"196",
    u"deep_pink_2": u"197",
    u"deep_pink_1a": u"198",
    u"deep_pink_1b": u"199",
    u"magenta_2b": u"200",
    u"magenta_1": u"201",
    u"orange_red_1": u"202",
    u"indian_red_1c": u"203",
    u"indian_red_1d": u"204",
    u"hot_pink_1a": u"205",
    u"hot_pink_1b": u"206",
    u"medium_orchid_1b": u"207",
    u"dark_orange": u"208",
    u"salmon_1": u"209",
    u"light_coral": u"210",
    u"pale_violet_red_1": u"211",
    u"orchid_2": u"212",
    u"orchid_1": u"213",
    u"orange_1": u"214",
    u"sandy_brown": u"215",
    u"light_salmon_1": u"216",
    u"light_pink_1": u"217",
    u"pink_1": u"218",
    u"plum_1": u"219",
    u"gold_1": u"220",
    u"light_goldenrod_2b": u"221",
    u"light_goldenrod_2c": u"222",
    u"navajo_white_1": u"223",
    u"misty_rose1": u"224",
    u"thistle_1": u"225",
    u"yellow_1": u"226",
    u"light_goldenrod_1": u"227",
    u"khaki_1": u"228",
    u"wheat_1": u"229",
    u"cornsilk_1": u"230",
    u"grey_100": u"231",
    u"grey_3": u"232",
    u"grey_7": u"233",
    u"grey_11": u"234",
    u"grey_15": u"235",
    u"grey_19": u"236",
    u"grey_23": u"237",
    u"grey_27": u"238",
    u"grey_30": u"239",
    u"grey_35": u"240",
    u"grey_39": u"241",
    u"grey_42": u"242",
    u"grey_46": u"243",
    u"grey_50": u"244",
    u"grey_54": u"245",
    u"grey_58": u"246",
    u"grey_62": u"247",
    u"grey_66": u"248",
    u"grey_70": u"249",
    u"grey_74": u"250",
    u"grey_78": u"251",
    u"grey_82": u"252",
    u"grey_85": u"253",
    u"grey_89": u"254",
    u"grey_93": u"255",

}


def FG_COLOURS(name):
    return u"38;5;{}".format(COLOURS[name])


def BG_COLOURS(name):
    return u"48;5;{}".format(COLOURS[name])



