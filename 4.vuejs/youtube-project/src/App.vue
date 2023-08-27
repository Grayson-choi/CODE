<template>
  <div id="app">
  <header>
  <SearchBar @input-search="onInputSearch" :videos-length="videos.length"/>
  </header>
  <section>
  <VideoDetail :video="selectedVideo"/>
  <VideoList :videos="videos" @select-video="onVideoSelect"/>
  </section>
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from '@/components/SearchBar'
import VideoList from '@/components/VideoList'
import VideoDetail from '@/components/VideoDetail'


const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'



export default {
  name: 'App',
  components: {
    SearchBar,
    VideoList, 
    VideoDetail,
  },
  data: function () {
    return {
      inputValue: '',
      selectedVideo: '',
      videos: [],
    }
  },
   methods: {
    onInputSearch: function (inputText) {
      this.inputValue = inputText
            const params = {
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: this.inputValue,
      }

      axios.get(API_URL, {
        // params: params,
        params,
      })
      .then((res) => {
        // console.log(res)
				// console.log(res.data.items)
        this.videos = res.data.items
        if (!this.selectedVideo) {
            this.selectedVideo = this.videos[0]
          }
      })
      .catch((err) => {
        console.log(err)
      })
    },
    onVideoSelect: function (video) {
      this.selectedVideo = video
    }
  }
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

section,
header {
  width: 80%;       /* 전체 너비의 80% */
  margin: 0 auto;   /* 양 옆 margin을 균등하게 배분*/
  padding: 1rem 0;  /* 위, 아래 padding */
}

section {
  display: flex;  /* Detail, List를 가로 배치 */
}
</style>
