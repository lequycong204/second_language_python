def restore_string(chars, freq):
    """
    Từ một chuỗi gốc được nén thành 2 danh sách chars và freq.
    chars: một danh sách các ký tự kiểu dữ liệu str
    freq: một danh số lần xuất hiện tương ứng các ký tự trong chuỗi gốc, kiểu dữ liệu str
    
    Hãy khôi phục lại chuỗi gốc ban đầu.
    Nếu danh sách số lần xuất hiện (freq) thừa / thiếu so với danh sách chars thì trả về chuỗi "ERROR"
    
    Ví dụ:
    input:
    chars: ['a','b','c','d']
    freq: ['1','4','0','2']
    output: abbbbdd
    
    chars: ['a','b','c','d']
    freq: ['1','4','2','2']
    output: abbbbccdd
    
    chars: ['a','b','c','d']
    freq: ['1','4','0']
    output: ERROR
    
    chars: ['a','b','c','d']
    freq: ['1','4','0','2','3']
    output: ERROR
    """

    if len(chars) != len(freq):
        return "ERROR"

    result = ""

    for i in range(len(chars)):
        temp = chars[i] * int(freq[i])
        result += str(temp)

    return result

# chars= ['a','b','c','d']
# freq= ['1','4','0','2','3']
# a =restore_string(chars, freq)
# print(a)

def find_min_word(wordFreq):
    """
    Đầu vào là một từ điển có khóa là từ, giá trị là số lần xuất hiện của từ đó trong 1 doccument.
    Hãy trả về từ có số lần xuất hiện ít nhất trong từ điển
    
    Nếu có 2 từ cùng số lần xuất hiện ít nhất, trả ra từ bé hơn theo thứ tự trong từ điển. (từ bé hơn theo bảng mã ASCII)
    
    Ví dụ:
    input: {'busy': 11, 'actor': 10, 'parent': 11, 'point': 11, 'slow': 10}
    output: actor
    """

    freq = list(wordFreq.values())

    min_freq = min(freq)
    result = []
    for k, v in wordFreq.items():
        if v == min_freq:
            result.append(k)
    result.sort()
    return result[0]

# wordFreq = {'urban': 10, 'retain': 9, 'complain': 10, 'his': 10, 'shoulder': 10, 'ability': 10, 'college': 8, 'sake': 9, 'conservative': 8, 'edge': 11}
# wordFreq ={'ignore': 11, 'language': 10, 'Mr': 11, 'freedom': 8, 'etc': 11, 'clothes': 11, 'freeze': 8, 'assert': 11, 'hit': 10, 'power': 8}
#wordFreq ={'flag': 11, 'eat': 9, 'all': 9, 'constantly': 11, 'observer': 10, 'popular': 9, 'thought': 11, 'tobacco': 10, 'window': 10, 'university': 9}
#Pass wordFreq ={'recover': 9, 'base': 10, 'message': 9, 'injury': 10, 'mere': 11, 'mystery': 8, 'item': 10, 'meaning': 10, 'trust': 10, 'vegetable': 10}
# wordFreq ={'gaze': 10, 'soldier': 11, 'through': 10, 'finance': 9, 'employ': 10, 'ready': 8, 'effective': 8, 'pain': 10, 'retire': 10, 'ice': 9}
#wordFreq ={'low': 10, 'flower': 9, 'treaty': 11, 'prepare': 8, 'sink': 11, 'negative': 10, 'gather': 8, 'online': 11, 'gesture': 9, 'chip': 11}

#wordFreq = {'busy': 11, 'actor': 10, 'parent': 11, 'point': 11, 'slow': 10}
# print(find_min_word(wordFreq))

def find_abundant_number(matrix):
    """
    matrix là một danh sách gồm n phần tử trong đó mỗi phần tử là một danh sách n số nguyên.
    Có thể hình dung matrix như một ma trận vuông có số chiều là (n, n).
    
    Hãy tìm và trả về theo thứ tự tăng dần về giá trị các số dư thừa nằm trong 
    MA TRẬN TAM GIÁC DƯỚI của matrix
    
    Số dư thừa là số có tổng các ước (không tính chính nó) lớn hơn 
    số đó.
    Ví dụ: 12 là số dư thừa do (1 + 2 + 3 + 4 + 6) > 12
    18 là số dư thừa do (1 + 2 + 3 + 6 + 9) > 18
    
    Ví dụ: 
    input: [[10, 91, 55, 53, 89], 
           [57, 28, 45, 19, 74], 
           [32, 41, 84, 93, 62], 
           [28, 74, 66, 46, 29], 
           [37, 12, 69, 97, 1]]
           
    output: [12, 66, 84]
    """

    elements = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i >= j:
                elements.append(matrix[i][j])
    def is_abundant(n):
        if n < 1:
            return False
        sum = 0
        for i in range(1, n):
            if n % i == 0:
                sum += i
        return sum > n
    elements = [x for x in elements if is_abundant(x)]
    elements.sort()
    return elements

# matrix = [[10, 91, 55, 53, 89],
#          [57, 28, 45, 19, 74], 
#            [32, 41, 84, 93, 62], 
#            [28, 74, 66, 46, 29], 
#            [37, 12, 69, 97, 1]]
# print(find_abundant_number(matrix))


def sort_two_four(arr):
    """
    arr là một danh sách các số nguyên. hãy sắp xếp các phần tử trong danh sách theo quy tắc sau:
    
    các số chia hết cho 4 về đầu danh sách, 
    các số chia hết cho 2 nhưng không chia hết cho 4. về cuối danh sách
    Số chia hết cho 4 giảm dần chia hết cho 2 tăng dần.
    
    Ví dụ:
    input: [4, 76, 98, 44, 92, 2, 68, 38, 86, 46]
    output: [92, 76, 68, 44, 4, 2, 38, 46, 86, 98]
    """

    num_top = []
    num_bot = []

    for i in arr:
        if i % 4 == 0:
            num_top.append(i)
        elif i % 2 == 0:
            num_bot.append(i)
    num_top.sort(reverse=True)
    num_bot.sort()
    return num_top + num_bot

# arr = [4, 76, 98, 44, 92, 2, 68, 38, 86, 46]
# print(sort_two_four(arr))