let requests = window.performance.getEntriesByType("resource")
board_info_link = ''
requests.forEach((value, index) => {
    if (value['name'].includes('BoardFeedResource')) {
        board_info_link = value["name"]
    }
})
board_info_link = decodeURIComponent(board_info_link)
board_info_link = board_info_link.replace('\"page_size\":25', '\"page_size\":250')
console.log(board_info_link)