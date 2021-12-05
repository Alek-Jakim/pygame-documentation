```gdscript


# Static Body is for something static duuuh

var motion = Vector2()
const GRAVITY = 20
const SPEED = 200
const JUMP_HEIGHT = -600
const UP = Vector2(0, -1)



func _physics_process(delta):
	
	motion.y += GRAVITY
	
	if Input.is_action_pressed("ui_right"):
		motion.x = SPEED
	elif Input.is_action_pressed("ui_left"):
		motion.x = -SPEED
	else:
		motion.x = 0
		
	if is_on_floor():
		if Input.is_action_just_pressed("ui_up"):
			motion.y = JUMP_HEIGHT	
	
	motion = move_and_slide(motion, UP)
	pass

```