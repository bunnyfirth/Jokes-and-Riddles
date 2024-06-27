questions = [
	'why did the chicken cross the road?',
	'why did the fish cross the sea?',
        'did you hear about the cat who sucked a lemon?',
        'why do elephants not like playing cards in the jungle',
        'did you hear about the crocadile with the camera',	
		'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
		'WABA DABA DOO! I SEE YOU!',
		'What is a cheese?'
]

answers = [
	'to get to the other side!',
	'to get to the other tide!',
        'he was a sourpuss!',
        'because of all the cheetas!',
        'he was snap-happy!',
		'Its the alphabet!',
		'THE END',
		'a chesse is a solad block of milk. i spelled soled wrong, didn\'t i?'
]

i = 0
while i < len(questions):
	print('Q: ' + questions[i])
	text = input('')
	print('A: ' + answers[i])
	i += 1