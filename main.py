def createEnemy():
    global enemySprite1
    enemySprite1 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    animation.run_image_animation(enemySprite1,
        assets.animation("""
            myAnim0
        """),
        200,
        True)
    tiles.place_on_random_tile(enemySprite1, sprites.dungeon.button_orange_depressed)
    enemySprite1.follow(mySprite, 50)

def on_on_overlap(sprite, otherSprite):
    music.siren.play()
    game.over(False, effects.slash)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap)

enemySprite1: Sprite = None
mySprite: Sprite = None
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
animation.run_image_animation(mySprite, assets.animation("""
    myAnim
"""), 200, True)
tiles.set_current_tilemap(tilemap("""
    level1
"""))
tiles.place_on_tile(mySprite, tiles.get_tile_location(8, 8))
createEnemy()

def on_on_update():
    controller.move_sprite(mySprite, 200, 200)
    scene.camera_follow_sprite(mySprite)
    if game.runtime() >= 10000:
        game.over(True, effects.confetti)
game.on_update(on_on_update)

def on_update_interval():
    pass
game.on_update_interval(5000, on_update_interval)
