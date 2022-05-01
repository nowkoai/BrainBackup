const startBtn = document.querySelector('#start-btn');
const stopBtn = document.querySelector('#stop-btn');
const resultDiv = document.querySelector('#result-div');

SpeechRecognition = webkitSpeechRecognition || SpeechRecognition;
let recognition = new SpeechRecognition();

recognition.lang = 'ja-JP';
recognition.interimResults = true;
recognition.continuous = true;

let finalTranscript = ''; // 確定した(黒の)認識結果

recognition.onresult = (event) => {
  let interimTranscript = ''; // 暫定(灰色)の認識結果
  let finalTranscript = ''; // 確定した(黒の)認識結果
  for (let i = event.resultIndex; i < event.results.length; i++) {
    let transcript = event.results[i][0].transcript;
    if (event.results[i].isFinal) {
      finalTranscript = transcript;
    } else {
      interimTranscript = transcript;
    }
  }
  let input_text = finalTranscript;
  let task_text = input_text.replace("をタスクに追加","");//タスクの文字を消す
  post_text.value = task_text + interimTranscript;

  if(finalTranscript.endsWith('をタスクに追加')||finalTranscript.endsWith('な')){
    //ここに追加する処理
    const url = '{% url "app:add" %}'
    const post_text = document.getElementById('post_text')
    // URLのクエリパラメータを管理
    const body = new URLSearchParams()
    body.append('text', post_text.value)

    fetch(url, {
      method: 'POST',
      body: body,
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        'X-CSRFToken': csrftoken,
      },
    })
      .then((response) => {
        // JSON形式に変換
        return response.json()
      })
      .then((response) => {
        // フォームをクリア
        post_text.value = ''
        // 追加するエレメント
        const postArea = document.getElementById('posts');
        const element = Object.assign(document.createElement('div'), { className: 'wra' });
        const element2 = Object.assign(document.createElement('div'), { className: 'wrap' });
        const element3 = Object.assign(document.createElement('div'), { className: 'wrapper' });

        const element4 = Object.assign(document.createElement('input'))
        element4.setAttribute('id', 'new');
        element4.setAttribute('type','checkbox')
        const element5 = Object.assign(document.createElement('label'), { textContent: response.text,})
        element5.htmlFor = 'new';
        element.appendChild(element2)
        element2.appendChild(element3)
        element3.appendChild(element4)
        element3.appendChild(element5)
        // 最後に追加
        postArea.insertBefore(element, postArea.lastChild.nextSibling)
        
      })
      
      .catch((error) => {
        console.log(error)
      })
      
  }

  
}

//ページが読み込まれたら音声認識を開始
recognition.start();

// https://developer.mozilla.org/ja/docs/Learn/JavaScript/Client-side_web_APIs/Fetching_data

// CSRF対策
const getCookie = (name) => {
  if (document.cookie && document.cookie !== '') {
    for (const cookie of document.cookie.split(';')) {
      const [key, value] = cookie.trim().split('=')
      if (key === name) {
        return decodeURIComponent(value)
      }
    }
  }
}
const csrftoken = getCookie('csrftoken')

// 記事追加キーボードバージョン
const addNeuron = document.getElementById('add_neuron')
addNeuron.addEventListener('submit', (e) => {
  e.preventDefault()
  const url = '{% url "app:add" %}'
  const post_text = document.getElementById('post_text')
  // URLのクエリパラメータを管理
  const body = new URLSearchParams()
  body.append('text', post_text.value)

  fetch(url, {
    method: 'POST',
    body: body,
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
      'X-CSRFToken': csrftoken,
    },
  })
    .then((response) => {
      // JSON形式に変換
      return response.json()
    })
    .then((response) => {
      // フォームをクリア
      post_text.value = ''
      // 追加するエレメント
      const postArea = document.getElementById('posts')
      const element = Object.assign(document.createElement('div'), { className: 'wra' })
      const element2 = Object.assign(document.createElement('div'), { className: 'wrap' })
      const element3 = Object.assign(document.createElement('div'), { className: 'wrapper' })

      const element4 = Object.assign(document.createElement('input'))
        element4.id = "{{ neuron.id }}"
        element4.setAttribute('type','checkbox')
      const element5 = Object.assign(document.createElement('label'), { textContent: response.text,})
        element5.for="{{ neuron.id }}"

      element.appendChild(element2)
      element2.appendChild(element3)
      element3.appendChild(element4)
      element3.appendChild(element5)
      // 最後に追加
      postArea.insertBefore(element, postArea.lastChild.nextSibling)
    })
    .catch((error) => {
      console.log(error)
    })
})