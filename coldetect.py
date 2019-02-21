def check_player_pillar_collision(player_x, player_y, pillar_x, pillar_y):
    """
    When the dot is very far left of the pillar pair
 
    >>> check_player_pillar_collision(100, 100, 300, 200)
    False
 
    When the dot hit the middle of the top pillar
 
    >>> check_player_pillar_collision( 300, 300, 300, 200 )
    True

    """
    if pillar_x-40 < player_x < pillar_x+40 and not (pillar_y - 100 < player_y < pillar_y + 100):
        return True
    else:
        return False
    