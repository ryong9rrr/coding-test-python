# 202ms(99.30%), 16.8MB(10.57%)
class BrowserHistory:

    def __init__(self, homepage: str):
        self.visited_urls = [homepage]
        self.current_index = 0

    def visit(self, url: str) -> None:
        self.visited_urls = self.visited_urls[0 : self.current_index + 1]
        self.visited_urls.append(url)
        self.current_index += 1

    def back(self, steps: int) -> str:
        self.current_index = max(self.current_index - steps, 0)
        return self.visited_urls[self.current_index]

    def forward(self, steps: int) -> str:
        self.current_index = min(self.current_index + steps, len(self.visited_urls) - 1)
        return self.visited_urls[self.current_index]
