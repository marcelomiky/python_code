class ViradaCulturalSpider(CrawlSpider):
    name = "virada_cultural"
    start_urls = ["http://conteudo.icmc.usp.br/Portal/conteudo/484/243/alunos-especiais"]

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
