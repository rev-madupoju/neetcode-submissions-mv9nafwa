class Solution:
    def search(self, N: List[int], T: int) -> int:
        l, r = 0, len(N) - 1

        while l <= r:
            mid = (l + r) // 2

            if N[mid] == T:
                return mid

            if N[l] > N[mid]:
                if N[l] <= T < N[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if N[mid] < T <= N[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1


