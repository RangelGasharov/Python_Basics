def news_at_ten(text, screen_width):
    current_word = screen_width * " "
    result = [current_word]
    for i in range(len(text)):
        current_word = current_word[1:] + text[i]
        result.append(current_word)
    for i in range(screen_width):
        current_word = current_word[1:] + " "
        result.append(current_word)
    return result


def print_headlines(headlines):
    for headline in headlines:
        print(headline)


print_headlines(news_at_ten("123456789", 6))
print_headlines(news_at_ten('edabit', 10))
print_headlines(news_at_ten('The latest news from News at Ten', 17))
print_headlines(news_at_ten('Woman singlehandedly boosts seaside town economy with sea-shell business!', 7))
print_headlines(news_at_ten('news', 30))
print_headlines(news_at_ten('Hello World', 11))
