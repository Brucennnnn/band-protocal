def chicken_rescue(c, s):
        n = len(c)
        max_chickens = 0
        left = 0

        for right in range(n):
            while c[right] - c[left] + 1 > s:
                left += 1
            max_chickens = max(max_chickens, right - left + 1)

        return max_chickens
