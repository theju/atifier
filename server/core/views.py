import time
import os
import subprocess
import tempfile

from .models import PageScrapeResult


def scrape_url(page):
    script_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), "../../scraper/hasher.js"
        )
    )
    cwd = os.path.dirname(script_path)
    script = os.path.basename(script_path)
    outfd = tempfile.SpooledTemporaryFile()
    try:
        proc = subprocess.Popen(
            ["node", script, page.url, page.selector],
            stdout=outfd,
            cwd=cwd
        )
    except Exception as ex:
        return None

    start_time = time.time()
    while proc.poll() is None:
        if time.time() - start_time > page.interval * 60:
            proc.terminate()
            break
        time.sleep(1)

    outfd.seek(0)
    output = outfd.read().strip()
    outfd.close()
    if len(output) == 0:
        return None
    try:
        hd, content = output.split("|||", 1)
    except ValueError:
        return None
    if not page.pagescraperesult_set.count():
        latest_scrape = PageScrapeResult()
    else:
        latest_scrape = page.pagescraperesult_set.all()[0]
    if latest_scrape.hash != hd:
        PageScrapeResult.objects.create(
            page=page,
            output=content,
            hash=hd
        )
