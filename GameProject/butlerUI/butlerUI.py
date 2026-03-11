from .butlerIntro import butler_intro
from .butlerAdvice1 import butler_npc_advice
from .butlerAdvice2 import butler_travel_advice
from .butlerAdvice3 import butler_player_death
from .butlerAdvice4 import butler_after_history
from .butlerAdvice5 import butler_choose_empire
from .butlerLoaded import butler_loaded_game
from .butlerFirstItem import butler_first_demonic_spirit
from .butlerNew import butler_new_game
from .butlerGoodBye import goodbye_saved, warn_unsaved
from .butlerHint import lucifer_hint
from .butlerSummon import butler_summon
from .butlerPlayer import who_player, player_role
from .butlerButler import butler_role, who_is_butler
from .butlerFail import butler_invalid_choice

def butler_1():
    butler_intro()

def butler_2():
    butler_npc_advice()

def butler_3(player_gold, travel_cost):
    butler_travel_advice(player_gold, travel_cost)

def butler_4():
    butler_player_death()

def butler_5():
    butler_after_history()

def butler_6():
    butler_new_game()

def butler_7():
    butler_loaded_game()

def butler_8():
    butler_choose_empire()

def butler_9():
    butler_first_demonic_spirit()

def butler_10(save_id):
    goodbye_saved(save_id)

def butler_11():
    warn_unsaved()

def butler_12():
    lucifer_hint()

def butler_13():
    butler_summon()

def butler_14():
    player_role()

def butler_15():
    who_player()

def butler_16():
    who_is_butler()

def butler_17():
    butler_role()

def butler_18():
    butler_invalid_choice()