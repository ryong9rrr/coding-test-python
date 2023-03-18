// 178ms(81.11%), 52MB(82.22%)
class BrowserHistory {
  visitedUrls: string[]
  currentIndex: number

  constructor(homepage: string) {
    this.visitedUrls = [homepage]
    this.currentIndex = 0
  }

  visit(url: string): void {
    this.visitedUrls = this.visitedUrls.slice(0, this.currentIndex + 1)
    this.visitedUrls.push(url)
    this.currentIndex += 1
  }

  back(steps: number): string {
    this.currentIndex = Math.max(this.currentIndex - steps, 0)
    return this.visitedUrls[this.currentIndex]
  }

  forward(steps: number): string {
    this.currentIndex = Math.min(
      this.currentIndex + steps,
      this.visitedUrls.length - 1,
    )
    return this.visitedUrls[this.currentIndex]
  }
}
