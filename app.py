from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

alphabet = list("abcdefghijklmnopqrstuvwxyz")

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
   
    
def caesar_cipher(plain_text, shift_amount, encode_or_decode):
    output_text = ""
    
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in plain_text:
        if letter not in alphabet:
            output_text += letter
        else:
            position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            output_text += alphabet[position]
        # else:
        #     position = alphabet.index(letter) + shift_amount
        #     position %= len(alphabet)
        #     output_text += alphabet[position]
    return output_text
    
# should_continue = True

# while should_continue:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
    
#     caesar_cipher(plain_text=text, shift_amount=shift, encode_or_decode=direction)
    
#     restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
#     if restart == "no":
#         should_continue = False
#         print("Take Care")
    
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cipher', methods=['POST'])
def cipher():
    data = request.get_json()
    text = data.get('text', '')
    shift = int(data.get('shift', 0))
    direction = data.get('direction', 'encode')

    result = caesar_cipher(plain_text=text, shift_amount=shift, encode_or_decode=direction)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)    
    