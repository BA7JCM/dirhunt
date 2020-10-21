from dirhunt.pool import Pool


class Source(Pool):
    def __init__(self, result_callback, error_callback, max_workers=None):
        super(Source, self).__init__(max_workers)
        self.result_callback = result_callback
        self.error_callback = error_callback

    async def add_domain(self, domain):
        await self.submit(domain)

    def callback(self, domain):
        raise NotImplementedError

    def add_result(self, url):
        if self.result_callback:
            self.result_callback(url)

    def add_error(self, message):
        if self.error_callback:
            self.error_callback(message)
