import axios from 'axios';

interface InfoJSON{
    Websitename: string;
    WebsiteUrl: string;
    Time: string
}

interface Info{
    websitename: string;
    websiteurl: string;
    time: string;
}

function decodeUser(json: InfoJSON): Info {
  return {
    websitename:    json.Websitename,
    websiteurl:     json.WebsiteUrl,
    time: json.Time
  };
}

function getSearchHistory() {
    return ajax.get<InfoJSON[]>('http://127.0.0.1:8000/seeHistory/Crawl/').then(data => {
        return data.data.map(decodeUser);
    });
}

getSearchHistory()