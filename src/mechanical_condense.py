import re
import nltk

def is_noun(word):
    # Tokenize the word
    word_tokenized = nltk.word_tokenize(word)
    # Get the POS tag of the word
    tag = nltk.pos_tag(word_tokenized)[0][1]
    # Check if the tag corresponds to a noun
    return tag in ['NN', 'NNS', 'NNP', 'NNPS']

def is_unit(word):
    unit_names = ['meters','meter','feet','foot','inches','inch']
    return word in unit_names

def get_all_words(sentence):
    #split at punctuation
    split_sentence = re.split(r'[.?!]', sentence)
    #remove empty strings
    split_sentence = [x for x in split_sentence if x]
    #loop through each sentence
    all_words = []
    for ss in split_sentence:
        #split at spaces
        words = ss.split()
        #remove empty strings
        words = [x for x in words if x]
        #loop through each word
        for word in words:
            all_words.append(word)
    return all_words

def get_condensed_variables(sentence):
    condensed_parts = []
    #get all words
    all_words = get_all_words(sentence)
    #get indexes of words that are numbers
    number_indexes = [i for i, x in enumerate(all_words) if x.isdigit()]
    #loop each number
    for ni in number_indexes:
        #get the two words before and after the number
        #make sure you are checking within the bounds of the list
        if 3 <= ni:
            dx_left = 3
        elif 2 <= ni:
            dx_left = 2
        elif ni == 1:
            dx_left = 1
        else:
            dx_left = 0

        if ni <= len(all_words)-4:
            dx_right = 3
        elif ni <= len(all_words)-3:
            dx_right = 2
        elif ni == len(all_words)-2:
            dx_right = 1
        else:
            dx_right = 0
        before = all_words[ni-dx_left:ni]
        after = all_words[ni+1:ni+dx_right+1]

        #check if words before and after are nouns
        #loop through each word
        variables = []
        unit = None
        for w in before + after:
            #check if word is a noun
            if is_unit(w):
                unit = w
                continue
            if is_noun(w):
                variables.append(w)
        #join variables into a string separated by an underscore
        variable = '_'.join(variables)
        if variable == 'height':
            variable = 'vertical_displacement'
        condensed_parts.append(f'{variable}={all_words[ni]} {unit}')
    condensed = ';'.join(condensed_parts)
    return condensed

def get_desired_variable(sentence):
    #split at punctuation
    split_sentences = re.split(r'[.?!]', sentence)
    #remove empty strings
    split_sentences = [x for x in split_sentences if x]
    for s in split_sentences:
        #split at spaces
        words = s.split()
        #remove empty strings
        words = [x.lower() for x in words if x]
        if 'how' in words or 'what' in words:
            if 'long' in words:
                if 'take' in words:
                    return 'time'
            if 'far' in words:
                if 'travel' in words:
                    return 'distance'
            if 'fast' in words:
                if 'travel' in words:
                    return 'speed'
            if 'heavy' in words:
                if 'weigh' in words:
                    return 'mass'
            if 'big' in words:
                if 'measure' in words:
                    return 'size'
            if 'tall' in words:
                if 'measure' in words:
                    return 'height'
            if 'wide' in words:
                if 'measure' in words:
                    return 'width'
            if 'deep' in words:
                if 'measure' in words:
                    return 'depth'
            if 'hot' in words:
                if 'measure' in words:
                    return 'temperature'
            if 'cold' in words:
                if 'measure' in words:
                    return 'temperature'
            if 'much' in words:
                if 'measure' in words:
                    return 'amount'
            if 'many' in words:
                if 'measure' in words:
                    return 'amount'
    return None

def mechanical_condense(sentence):
    """
    Condenses a sentence by extracting only important information.
    Ex input= "An object is dropped from a height of 100 meters. How long does it take to reach the ground?"
    Ex output= "height=100 meters, desired_variable=time"
    """
    #get the condensed variables
    condensed_variables = get_condensed_variables(sentence)
    #get the desired variable
    desired_variable = get_desired_variable(sentence)
    #join the condensed variables and desired variable
    condensed = f'<start>{condensed_variables};desired_variable={desired_variable}<stop>'
    return condensed


if __name__ == '__main__':
    sentence = 'An object is dropped from a height of 100 meters. How long does it take to reach the ground?'
    condensed = mechanical_condense(sentence)
    print(condensed)