class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        n = len(foods)
        self.food2rate = { foods[i]:ratings[i] for i in range(n)}
        self.food2cusines = { foods[i]:cuisines[i] for i in range(n)}
        self.cuisinesMap = defaultdict(list)
        for i, cuisine in enumerate(cuisines):
            rating = ratings[i]
            food = foods[i]
            heappush(self.cuisinesMap[cuisine], (-1*rating, food ))
            
    def changeRating(self, food: str, newRating: int) -> None:
        self.food2rate[food] = newRating
        cuisine = self.food2cusines[food]
        heappush(self.cuisinesMap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        rating, food = self.cuisinesMap[cuisine][0]
        while rating != -1*self.food2rate[food]:  
            heappop(self.cuisinesMap[cuisine])
            rating, food = self.cuisinesMap[cuisine][0]
        return food


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)