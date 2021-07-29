#숫자 카드 게임
""" NxM 카드 더미에서 행 별로 낮은 카드 중 가장 높은 숫자 카드를 선택하라 """

n, m = map(int, input().split())
res = 0

big_card = 0
for i in range(n):
    cards = list(map(int, input().split()))
    if(big_card < min(cards)):
        big_card = min(cards)

print(big_card)
    
