---
layout: notebook-html
---

<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>멀티프로세싱에 강하다는 M1 pro 10 core CPU를 산 기념으로 어떻게 하면 모든 코어를 불타게 만들 수 있을까를 찾아보고 싶어졌다. 과연 10개의 코어를 모두 한꺼번에 돌리면 작업 수행 시간을 어디까지 줄일 수 있을까?</p>
<p>&nbsp;</p>
<p>시작하기 전에 내장 os 모듈을 이용해서 CPU core 개수를 확인해보자. 10개의 core가 잘 확인된다.</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[1]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>
<span class="n">os</span><span class="o">.</span><span class="n">cpu_count</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[1]:</div>




<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain">
<pre>10</pre>
</div>

</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<hr>
<h3 id="Mutiprocessing-module">Mutiprocessing module<a class="anchor-link" href="#Mutiprocessing-module">&#182;</a></h3><p>가장 먼저 파이썬에 내장된 multiprocessing 모듈을 사용해보자. 
목표는 0.01초가 걸리는 일을 1000번 반복하는 것이고 한 개의 프로세스로 시행한다면 10초 이상 걸린다.</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[14]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">time</span>
<span class="k">def</span> <span class="nf">simple_work</span><span class="p">(</span><span class="n">a</span><span class="p">):</span>
    <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mf">0.01</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[15]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="o">%%time</span>
<span class="k">for</span> <span class="n">a</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">1000</span><span class="p">):</span> 
    <span class="n">simple_work</span><span class="p">(</span><span class="n">a</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>CPU times: user 16.8 ms, sys: 9.02 ms, total: 25.8 ms
Wall time: 12 s
</pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>&nbsp;</p>
<p>multiprocessing에는 Process 클래스와 Pool 클래스가 있다. 
먼저 Process 클래스에서는 process에서 진행할 일들을 지정해 줘야 한다. 분리된 lst를 시행시킬 worker 함수를 만들고 python 파일로 저장하자.</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># test_work.py</span>
<span class="kn">import</span> <span class="nn">time</span>
<span class="k">def</span> <span class="nf">simple_work</span><span class="p">(</span><span class="n">a</span><span class="p">):</span>
    <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mf">0.01</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">simple_worker</span><span class="p">(</span><span class="n">divided_lst</span><span class="p">):</span>
    <span class="k">for</span> <span class="n">a</span> <span class="ow">in</span> <span class="n">divided_lst</span><span class="p">:</span>
        <span class="n">simple_work</span><span class="p">(</span><span class="n">a</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<blockquote><p>multiprocessing은 jupyter에서 그대로 사용 하면 AttributeError가 발생한다.
python 파일에서 시행하거나 시행할 함수를 .py 파일로 따로 만든 후 module로 불러와야 한다.</p>
</blockquote>

</div>
</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>&nbsp;</p>
<p>5개의 프로세스로 나눴더니 수행 시간이 5분의 1로 줄어들었다.</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[16]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">multiprocessing</span> <span class="kn">import</span> <span class="n">Process</span>
<span class="kn">from</span> <span class="nn">test_work</span> <span class="kn">import</span> <span class="n">simple_worker</span>

<span class="n">lst1</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">1000</span><span class="p">))</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[17]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="o">%%time</span>
<span class="n">processes</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">5</span><span class="p">):</span>
    <span class="n">p</span> <span class="o">=</span> <span class="n">Process</span><span class="p">(</span><span class="n">target</span><span class="o">=</span><span class="n">simple_worker</span><span class="p">,</span> <span class="n">args</span><span class="o">=</span><span class="p">(</span><span class="n">lst1</span><span class="p">[</span><span class="n">i</span><span class="o">*</span><span class="mi">200</span><span class="p">:(</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span><span class="o">*</span><span class="mi">200</span><span class="p">],))</span>
    <span class="n">p</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>
    <span class="n">processes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">p</span><span class="p">)</span>

<span class="k">for</span> <span class="n">process</span> <span class="ow">in</span> <span class="n">processes</span><span class="p">[:</span><span class="mi">1</span><span class="p">]:</span>
    <span class="n">process</span><span class="o">.</span><span class="n">join</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>CPU times: user 6.32 ms, sys: 35.8 ms, total: 42.1 ms
Wall time: 2.46 s
</pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>&nbsp;</p>

</div>
</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<hr>
<p>Pool 클래스는 process를 지정해서 나누는 수고를 덜어줘 더욱 간단하게 사용할 수 있다.</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[18]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">multiprocessing</span> <span class="kn">import</span> <span class="n">Pool</span>
<span class="kn">from</span> <span class="nn">test_work</span> <span class="kn">import</span> <span class="n">simple_work</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[19]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="o">%%time</span>
<span class="k">with</span> <span class="n">Pool</span><span class="p">(</span><span class="n">processes</span><span class="o">=</span><span class="mi">5</span><span class="p">)</span> <span class="k">as</span> <span class="n">pool</span><span class="p">:</span>
    <span class="n">pool</span><span class="o">.</span><span class="n">map</span><span class="p">(</span><span class="n">simple_work</span><span class="p">,</span> <span class="n">lst1</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>CPU times: user 13.4 ms, sys: 37.1 ms, total: 50.4 ms
Wall time: 2.52 s
</pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>&nbsp;</p>

</div>
</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<hr>
<p>이제 multiprocessing을 알게 되었으니 신나게 쓰려고 하다보면 이상함을 느끼게 된다. multiprocessing이 그냥 계산하는 것 보다 더 오래걸리는 것이다. 심지어 process 수를 늘렸더니 수행 시간이 더 늘어난다.</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[20]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">math</span>
<span class="n">lst2</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">1000000</span><span class="p">))</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[21]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="o">%%time</span>
<span class="n">result</span> <span class="o">=</span> <span class="p">[</span><span class="n">math</span><span class="o">.</span><span class="n">sqrt</span><span class="p">(</span><span class="n">a</span><span class="p">)</span> <span class="k">for</span> <span class="n">a</span> <span class="ow">in</span> <span class="n">lst2</span><span class="p">]</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>CPU times: user 97.8 ms, sys: 15.2 ms, total: 113 ms
Wall time: 112 ms
</pre>
</div>
</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[25]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="o">%%time</span>
<span class="k">with</span> <span class="n">Pool</span><span class="p">(</span><span class="n">processes</span><span class="o">=</span><span class="mi">5</span><span class="p">)</span> <span class="k">as</span> <span class="n">pool</span><span class="p">:</span>
    <span class="n">result</span> <span class="o">=</span> <span class="n">pool</span><span class="o">.</span><span class="n">map</span><span class="p">(</span><span class="n">math</span><span class="o">.</span><span class="n">sqrt</span><span class="p">,</span> <span class="n">lst2</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>CPU times: user 69.5 ms, sys: 74.6 ms, total: 144 ms
Wall time: 178 ms
</pre>
</div>
</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[24]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="o">%%time</span>
<span class="k">with</span> <span class="n">Pool</span><span class="p">(</span><span class="n">processes</span><span class="o">=</span><span class="mi">9</span><span class="p">)</span> <span class="k">as</span> <span class="n">pool</span><span class="p">:</span>
    <span class="n">result</span> <span class="o">=</span> <span class="n">pool</span><span class="o">.</span><span class="n">map</span><span class="p">(</span><span class="n">math</span><span class="o">.</span><span class="n">sqrt</span><span class="p">,</span> <span class="n">lst2</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>CPU times: user 77.4 ms, sys: 104 ms, total: 181 ms
Wall time: 189 ms
</pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>원인을 찾아 보았더니 multiprocessing에서 객체 전달 시스템의 문제라고 한다. multiprocess는 process spawning을 통해 자식 프로세스를 생성하고, 이 과정에서 데이터를 pickle을 사용해 직렬화 한 후 복사본을 만든다고 한다. 따라서 데이터가 클 수록, 프로세스가 늘어날 수록 걸리는 시간도 오래 걸리고 메모리 사용량도 늘어나게 된다. (10 core M1 pro를 산 이유가 없어지는 것이 아닌가!!!)</p>
<p>이 문제점을 해결할 방법을 찾다가 ray를 발견하게 되었다.</p>
<p>&nbsp;</p>
<hr>

</div>
</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h3 id="Ray">Ray<a class="anchor-link" href="#Ray">&#182;</a></h3><blockquote><p>ray는 multiprocessing에서 발생한 큰 오버헤드 문제를 해결하기 위해 zero-copy 직렬화를 수행하는 Apache Arrow를 사용한다고 한다. 자세한 설명은 reference에서 확인하자.  ( 
<a href="https://riiidtechblog.medium.com/ray-%ED%99%95%EC%9E%A5-%EA%B0%80%EB%8A%A5%ED%95%9C-%EA%B3%A0%EC%84%B1%EB%8A%A5-%EB%B6%84%EC%82%B0-%EB%B3%91%EB%A0%AC-machine-learning-%ED%94%84%EB%A0%88%EC%9E%84%EC%9B%8C%ED%81%AC-f17f9c9cbef3">[reference1]</a>
<a href="https://velog.io/@otzslayer/Ray%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%B4-Python-%EB%B3%91%EB%A0%AC-%EC%B2%98%EB%A6%AC-%EC%89%BD%EA%B2%8C-%ED%95%98%EA%B8%B0">[reference2]</a>)</p>
</blockquote>

</div>
</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>&nbsp;</p>
<p>ray를 사용하기 위해서는 4가지 과정이 필요하다.</p>
<p>(1) remote class를 사용하여 actor만들기</p>
<ul>
<li>원하는 function을 <code>@ray.remote</code> 데코레이터로 감싼다.</li>
</ul>
<p>(2) ray 시작하기 (ray.init)</p>
<p>(3) tasks(remote functions) 만들기</p>
<ul>
<li>1번에 만든 function을 .remote()로 호출하여 비동기적으로 시행할 remote function들을 만든다.</li>
</ul>
<p>(4) <code>ray.get</code>을 이용하여 result 가져오기</p>
<p>이 과정이 끝나면 <code>ray.shutdown()</code>을 꼭 실행해야 다음에 다시 ray를 불러올 수 있다.</p>
<p>&nbsp;</p>
<p>연산량에 비해 작업 반복 횟수가 많은 위의 예제는 ray에 적절하지 않다. 반복 횟수 만큼 remote function object를 만들기 때문에 그에 비례해 시간이 늘어난다. ray의 사용이 적절한 예는 아래와 같다.</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[50]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>

<span class="k">def</span> <span class="nf">make_rand_arr</span><span class="p">(</span><span class="n">num</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">rand</span><span class="p">(</span><span class="mi">1000</span><span class="p">,</span><span class="mi">1000</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">multiple_arr</span><span class="p">(</span><span class="n">arr1</span><span class="p">,</span><span class="n">arr2</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">arr1</span><span class="nd">@arr2</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[62]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="o">%%time</span>
<span class="n">result</span> <span class="o">=</span> <span class="p">[]</span>

<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">):</span>
    <span class="n">arr1</span> <span class="o">=</span> <span class="n">make_rand_arr</span><span class="p">(</span><span class="n">i</span><span class="p">)</span>
    <span class="n">arr2</span> <span class="o">=</span> <span class="n">make_rand_arr</span><span class="p">(</span><span class="n">i</span><span class="p">)</span>
    <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">multiple_arr</span><span class="p">(</span><span class="n">arr1</span><span class="p">,</span><span class="n">arr2</span><span class="p">))</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>CPU times: user 1.55 s, sys: 264 ms, total: 1.81 s
Wall time: 294 ms
</pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>&nbsp;</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[64]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">ray</span>

<span class="nd">@ray</span><span class="o">.</span><span class="n">remote</span>
<span class="k">def</span> <span class="nf">make_rand_arr</span><span class="p">(</span><span class="n">num</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">rand</span><span class="p">(</span><span class="mi">1000</span><span class="p">,</span><span class="mi">1000</span><span class="p">)</span>

<span class="nd">@ray</span><span class="o">.</span><span class="n">remote</span>
<span class="k">def</span> <span class="nf">multiple_arr</span><span class="p">(</span><span class="n">arr1</span><span class="p">,</span><span class="n">arr2</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">arr1</span><span class="nd">@arr2</span>
    
<span class="n">ray</span><span class="o">.</span><span class="n">shutdown</span><span class="p">()</span>
<span class="n">ray</span><span class="o">.</span><span class="n">init</span><span class="p">(</span><span class="n">num_cpus</span> <span class="o">=</span> <span class="mi">5</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[64]:</div>




<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain">
<pre>{&#39;node_ip_address&#39;: &#39;127.0.0.1&#39;,
 &#39;raylet_ip_address&#39;: &#39;127.0.0.1&#39;,
 &#39;redis_address&#39;: &#39;127.0.0.1:29059&#39;,
 &#39;object_store_address&#39;: &#39;/tmp/ray/session_2022-01-16_12-39-00_701759_2973/sockets/plasma_store&#39;,
 &#39;raylet_socket_name&#39;: &#39;/tmp/ray/session_2022-01-16_12-39-00_701759_2973/sockets/raylet&#39;,
 &#39;webui_url&#39;: None,
 &#39;session_dir&#39;: &#39;/tmp/ray/session_2022-01-16_12-39-00_701759_2973&#39;,
 &#39;metrics_export_port&#39;: 65485,
 &#39;node_id&#39;: &#39;12a2284120523d8a9f5dccf38be1f74b2001e524243d00d238034a04&#39;}</pre>
</div>

</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[65]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="o">%%time</span>
<span class="n">arr1_id</span> <span class="o">=</span> <span class="p">[</span><span class="n">make_rand_arr</span><span class="o">.</span><span class="n">remote</span><span class="p">(</span><span class="n">i</span><span class="p">)</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">)]</span>
<span class="n">arr2_id</span> <span class="o">=</span> <span class="p">[</span><span class="n">make_rand_arr</span><span class="o">.</span><span class="n">remote</span><span class="p">(</span><span class="n">i</span><span class="p">)</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">)]</span>
<span class="n">multi_id</span> <span class="o">=</span> <span class="p">[</span><span class="n">multiple_arr</span><span class="o">.</span><span class="n">remote</span><span class="p">(</span><span class="n">arr1</span><span class="p">,</span><span class="n">arr2</span><span class="p">)</span> <span class="k">for</span> <span class="n">arr1</span><span class="p">,</span> <span class="n">arr2</span> <span class="ow">in</span> <span class="nb">tuple</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span><span class="n">arr1_id</span><span class="p">,</span> <span class="n">arr2_id</span><span class="p">))]</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>CPU times: user 9.65 ms, sys: 4.72 ms, total: 14.4 ms
Wall time: 9.82 ms
</pre>
</div>
</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[66]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="o">%%time</span>
<span class="n">result</span> <span class="o">=</span> <span class="n">ray</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">multi_id</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>CPU times: user 1.71 ms, sys: 826 µs, total: 2.54 ms
Wall time: 1.43 ms
</pre>
</div>
</div>

</div>

</div>

</div>

&nbsp;

<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>병렬처리 하지 않았을 시 수행 시간은 300ms, ray 적용 시 10ms로 큰 차이를 보인다.</p>
<p>&nbsp;</p>
<hr>
<p>multiprocessing과는 더 큰 차이를 보인다.</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[31]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">multiprocessing</span> <span class="kn">import</span> <span class="n">Pool</span>
<span class="kn">from</span> <span class="nn">test_work2</span> <span class="kn">import</span> <span class="n">make_rand_arr</span><span class="p">,</span> <span class="n">multiple_arr</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[32]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="o">%%time</span>
<span class="k">with</span> <span class="n">Pool</span><span class="p">(</span><span class="n">processes</span><span class="o">=</span><span class="mi">5</span><span class="p">)</span> <span class="k">as</span> <span class="n">pool</span><span class="p">:</span>
    <span class="n">arr1</span> <span class="o">=</span> <span class="n">pool</span><span class="o">.</span><span class="n">map</span><span class="p">(</span><span class="n">make_rand_arr</span><span class="p">,</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">))</span>
    <span class="n">arr2</span> <span class="o">=</span> <span class="n">pool</span><span class="o">.</span><span class="n">map</span><span class="p">(</span><span class="n">make_rand_arr</span><span class="p">,</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">))</span>
    <span class="n">result</span> <span class="o">=</span> <span class="n">pool</span><span class="o">.</span><span class="n">starmap</span><span class="p">(</span><span class="n">multiple_arr</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span><span class="n">arr1</span><span class="p">,</span><span class="n">arr2</span><span class="p">)))</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>CPU times: user 208 ms, sys: 446 ms, total: 654 ms
Wall time: 1.06 s
</pre>
</div>
</div>

</div>

</div>

</div>
