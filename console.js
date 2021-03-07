board_info_link = ''
window.performance.getEntriesByType("resource").forEach((value) => { if (value['name'].includes('BoardFeedResource')) { board_info_link = value["name"] } })
console.log(decodeURIComponent(board_info_link).replace('\"page_size\":25', '\"page_size\":250'))