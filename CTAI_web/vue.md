@[TOC](VUE开发入门——手把手教你做一个备忘录网站)

# 本文禁止转载，违者必究！
# 1. 前言：
最近上了移动互联应用开发的专选课，结果大作业要求做一个前后端分离的项目。这边我是个小白，所以要从头开始学，目前打算做一个后端用Flask、前端用VUE的智能医疗项目。

因为医疗图像分割要用深度学习，所以用Python做后端开发比较方便，因此选用了Flask框架。而VUE是一套用于构建用户界面的渐进式框架。与其它大型框架不同的是，Vue 被设计为可以自底向上逐层应用。Vue 的核心库只关注视图层，不仅易于上手，还便于与第三方库或既有项目整合。另一方面，当与现代化的工具链以及各种支持类库结合使用时，Vue 也完全能够为复杂的单页应用提供驱动。

本博客主要是按照 [这个网站](https://developer.mozilla.org/zh-CN/) 的教程来的，里面写了项目完成的过程和自己的理解。

后记：大作业项目视频在这里~

[https://www.bilibili.com/video/BV1k54y1s7j9](https://www.bilibili.com/video/BV1k54y1s7j9)


[video(video-xqrrSDwe-1611656761668)(type-bilibili)(url-https://player.bilibili.com/player.html?aid=843751491)(image-https://ss.csdn.net/p?http://i1.hdslb.com/bfs/archive/4bd96281cb10ce1d6cf25c824711cbd4724c52f3.jpg)(title-基于Paddle+Flask的眼部医疗辅助系统（前后端分离）)]


# 2. VUE简介：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126184505626.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)

Vue是一个现代JavaScript框架提供了有用的设施渐进增强——不像许多其他框架，您可以使用Vue增强现有的HTML。这使我们可以使用Vue作为jQuery等库的临时替代品。

也就是说，我们还可以使用Vue编写整个单页应用程序(SPAs)。这允许我们创建标记完全由Vue管理,可以提高开发人员的经验和性能在处理复杂的应用程序。当我们需要的时候它还允许您利用其他库对客户端路由和状态进行管理。此外，Vue需要“中间地带”的方法工具客户端路由和状态管理。虽然Vue核心团队维护了建议的函数库，但他们并没有直接捆绑到 Vue 里。这样我们就可以选择一个其他路由/状态管理库，来更好地适应您的应用程序。

除了允许我们逐步将Vue集成到您的应用程序中,Vue还提供了一种渐进的方式编写标记。像大多数框架，Vue通过组件允许我们创建可重用块标记。大多数时候，Vue组件是使用一个特殊的HTML模板的语法写的。当我们需要比HTML语法允许的更多的控制时，我们可以编写JSX或纯JavaScript函数来定义组件。

# 3. VUE安装和环境配置：
要在现有站点中使用Vue，可以通过"script"元素在页面中直接使用。当使用JQuery这样的库将现有项目迁移到Vue时，这是一个很好的选择。通过这种方法，我们可以使用Vue的许多核心功能，例如属性、自定义组件和数据管理。

- 开发环境版本，包含了有帮助的命令行警告：

```html
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
```

- 生产环境版本，优化了尺寸和速度：

```html
<script src="https://cdn.jsdelivr.net/npm/vue@2"></script>
```

要构建更复杂的应用程序，我们需要使用 Vue NPM package。这将允许我们使用Vue的高级功能并利用WebPack等捆绑包。

为了使使用Vue构建应用程序更容易，有一个CLI来简化开发过程。要使用npm软件包和CLI：

- 安装Node.js：

> 在官网 [https://nodejs.org/en/](https://nodejs.org/en/) 下载即可安装

- 安装npm：

> npm已经在Node.js安装的时候顺带装好了。我们在命令提示符或者终端输入npm -v，应该看到类似的输出：

```bash
C:\>npm -v
4.1.2
```

- 安装CLI：

```bash
npm install --global @vue/cli
```

# 4. 创建VUE项目——Hello World：
## 4.1 创建基础项目：
使用如下命令创建一个项目：

```bash
vue create moz-todo-vue
```
选择Default配置：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126185516273.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)

然后脚手架工具就开始构建项目，并且安装所需的依赖：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126185627530.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)
创建完成后，可以看到出现了一些文件：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126190206798.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)
## 4.2 文件类型解析：
我们接下来列举一些比较重要的：
- **.eslintrc.js:** 这个是 eslint 的配置文件，可以通过它来管理你的校验规则。
- **babel.config.js:** 这个是 Babel 的配置文件，可以在开发中使用 JavaScript 的新特性，并且将其转换为在生产环境中可以跨浏览器运行的旧语法代码。你也可以在这个里配置额外的 babel 插件。 
- **.browserslistrc:** 这个是 Browserslist 的配置文件，可以通过它来控制需要对哪些浏览器进行支持和优化。
- **public:** 这个目录包含一些在 Webpack 编译过程中没有加工处理过的文件（有一个例外：index.html 会有一些处理）。
	- **favicon.ico:** 这个是项目的图标，当前就是一个 Vue 的 logo。
	- **index.html:** 这是应用的模板文件，Vue 应用会通过这个 HTML 页面来运行，也可以通过 lodash 这种模板语法在这个文件里插值。
- **src:** 这个是 Vue 应用的核心代码目录
	- **main.js:** 这是应用的入口文件。目前它会初始化 Vue 应用并且制定将应用挂载到  index.html 文件中的哪个 HTML 元素上。通常还会做一些注册全局组件或者添额外的 Vue 库的操作。
	- **App.vue:** 这是 Vue 应用的根节点组件，往下看可以了解更多关注 Vue 组件的信息。
	- **component:** 这是用来存放自定义组件的目录，目前里面会有一个示例组件。
	- **assets:** 这个目录用来存放像 CSS 、图片这种静态资源，但是因为它们属于代码目录下，所以可以用 webpack 来操作和处理。意思就是你可以使用一些预处理比如 Sass/SCSS 或者 Stylus。

## 4.3 .vue 文件（单文件组件）：
就像很多其他的前端框架一样，组件是构建 Vue 应用中非常重要的一部分。组件可以把一个很大的应用程序拆分为独立创建和管理的不相关区块，然后彼此按需传递数据，这些小的代码块可以方便更容易的理解和测试。

在其他框架都鼓励把模板、逻辑和样式的代码区分成不同文件的时候，Vue 却反其道行之。使用单文件组件，Vue 把模板、相关脚本和 CSS 一起整合放在 .vue 结尾的一个单文件中。这些文件最终会通过 JS 打包工具（例如 Webpack）处理，这意味着你可以使用构建时工具。我们可以使用比如 Babel、TypeScript、SCSS 等来创建更多复杂的组件。

 另外，使用 Vue CLI 创建的项目被配置为在开箱即用的情况下借助 Webpack 使用 .vue 文件。实际上，如果我们查看我们使用 CLI 创建的项目中的 src 文件夹，我们会看到第一个.vue 文件：App.vue：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126191710147.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)


打开 App.vue 文件，可以看到有三部分组成 "template"，"script" 和 "style"，分别包含了组件的模板、脚本和样式相关的内容。所有的单文件组件都是这种类似的基本结构。

- "template" 包含了所有的标记结构和组件的展示逻辑。template 可以包含任何合法的 HTML，以及一些我们接下来要讲的 Vue 特定的语法。
- "script" 包含组件中所有的非显示逻辑，最重要的是， "script" 标签需要默认导出一个 JS 对象。该对象是您在本地注册组件、定义属性、处理本地状态、定义方法等的地方。在构建阶段这个对象会被处理和转换（包含 template 模板）成为一个有 render() 函数的 Vue 组件。
- 组件的 CSS 应该写在 "style" 标签里，如果我们添加了 scoped 属性，形如 "style scoped" ，Vue 会把样式的范围限制到单文件组件的内容里。

## 4.4 运行项目：
在终端输入：

```bash
npm run serve
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126191945936.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)
然后打开Localhost，就可以看到VUE的Hello World界面：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126192024440.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)

## 4.5 打包项目：
在终端运行：

```bash
npm run build
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126192352340.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)
即可打包到dist文件夹：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126192401350.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)
# 5. 在网页中显示标题：
在前面我们讲过， "template" 包含了所有的标记结构和组件的展示逻辑，可以包含任何合法的 HTML。因此我们可以用 HTML 修改  "template" 以显示标题。

因此我们将 "template" 修改为：

```html
<template>
  <div id="app">
    <h1>备忘录</h1>
  </div>
</template>
```

这时我们重新运行项目（或者项目在一个终端一直开着）：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126192922755.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)

发现运行出错！

这是因为 VUE 中如果某一个组件导入（HelloWorld.vue）而未使用时，VUE 编译不会通过，因此我们要删掉 "script" 中的 HelloWorld，将其修改为：

```html
<script>
export default {
  name: "App",
};
</script>
```

这样就可以看到终端中编译通过：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126193115590.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)
同时 Localhost 的内容几乎也会同时更新：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126193229991.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)
# 6. 添加待做事项：
这部分我们将从创建一个组件来表示待办事项列表中的每个项目开始。在这一过程中，我们将学习一些重要的概念，例如在其他组件中调用组件，通过道具向它们传递数据，以及保存数据状态。

## 6.1 创建一个ToDoItem组件：
让我们创建第一个组件，它将显示一个单一的待办事项。我们将用它来建立我们的待办事项列表。

1. 在我们的的 src/components 目录下，创建一个ToDoItem.vue的新文件。
2. 通过在文件顶部添加 "template""/template"来创建组件的模板部分。
在我们的模板部分下面创建一个"script""/script"部分。
3. 在"script"标签内，添加一个默认导出对象export default {}，这就是我们的组件对象。

现在 ToDoItem.vue 应该是这样：

```html
<template></template>
<script>
export default {};
</script>
```

现在我们可以开始为ToDoItem添加实际内容了。Vue模板目前只允许一个根元素——一个元素需要包裹模板内的所有内容（Vue 3 后允许多个）。

我们将为该根元素使用一个"div"。

1. 现在在我们的组件模板中添加一个空的"div"。

2. 在"div"里面，让我们添加一个checkbox和一个对应的label。给复选框添加一个id，并添加一个for属性，将复选框映射到标签上。

现在 ToDoItem.vue 应该是这样：

```html
<template>
  <div>
    <input type="checkbox" id="todo-item" checked="false" />
    <label for="todo-item">我的待做事项</label>
  </div>
</template>
```
## 6.2 在应用程序中使用TodoItem组件：
我们现在把TodoItem组件添加到我们的主程序中：
1. 再次打开App.vue文件。
2. 在"script"标签的顶部，添加以下内容来引入ToDoItem组件：
	

	> import ToDoItem from './components/ToDoItem.vue';

3. 在我们的组件对象里面，添加 components 属性，然后在它里面添加我们的ToDoItem组件进行注册：
	> components: {ToDoItem,}

现在 App.vue 应该是这样：

```html
<template>
  <div id="app">
    <h1>备忘录</h1>
  </div>
</template>

<script>
import ToDoItem from "./components/ToDoItem.vue";
export default {
  name: "App",
  components: {
    ToDoItem,
  },
};
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
</style>

```

而要在应用程序中实际展示ToDoItem组件，我们需要在"template"模板内添加一个"to-do-item""/to-do-item"元素。请注意，组件文件名及其在JavaScript中的表示方式总是用驼峰大写（例如ToDoList），而等价的自定义元素总是用连字符小写（例如"to-do-list"）：
1. 在"h1"下面，创建一个无序列表("ul")，其中包含一个列表项("li")。
2. 在列表项("li")里面添加"to-do-item""/to-do-item"。

现在 App.vue 应该是这样：

```html
<template>
  <div id="app">
  <h1>备忘录</h1>
  <ul>
    <li>
      <to-do-item></to-do-item>
    </li>
  </ul>
</div>
</template>

<script>
import ToDoItem from "./components/ToDoItem.vue";
export default {
  name: "App",
  components: {
    ToDoItem,
  },
};
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
</style>

```
如果我们再次查看你的应用程序的渲染情况，现在应该看的到渲染的ToDoItem组件，由一个复选框和一个标签组成：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126194531820.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)
## 6.3 使用props使组件动态化：
这时我们会发现一个问题，就是我们的ToDoItem组件只能在页面上真正包含一次（ID必须是唯一的），并且我们无法设置标签文本，没有什么是动态的。

因此我们需要一些组件状态。这可以通过在我们的组件中添加props来实现。我们可以认为props类似于函数中的输入，props的值赋予组件一个影响其显示的初始状态。

在Vue中，有两种注册props的方法：
1. 第一种方法是将props列为字符串数组。数组中的每个条目都对应于props的名称。
2. 第二种方法是将props定义为一个对象，每个键对应于prop名称。将props列为对象可让我们指定默认值，根据需要标记props，执行基本的对象键入（特别是围绕JavaScript基本类型）以及执行简单的prop验证。

对于此组件，我们将使用对象注册方法。
1. 返回ToDoItem.vue文件。
2. 在导出default {}对象内部添加一个props属性，该属性包含一个空对象。
3. 在此对象内，使用键label和添加两个属性done，label代表待做事项的名称，done代表事情是否完成。
4. label键的值应是具有2个属性的对象（或props，因为他们是所谓的在被提供给部件的上下文中）。
	1. 第一个是required属性，其值为true。这将告诉Vue，我们希望该组件的每个实例都有一个label字段。如果ToDoItem组件没有标签字段，Vue会警告我们。
	2. 第二个是type属性。将此属性的值设置为JavaScriptString类型（注意，大写字母“ S”）。这告诉Vue，我们希望此属性的值为字符串。
5. 现在到done。
	1. 首先添加一个default值为的字段false。这意味着，当没有任何done prop传递到ToDoItem组件时，done prop的默认值将为false。
	2. 接下来，添加一个type值为的字段Boolean。这告诉Vue，我们期望value prob是JavaScript布尔类型。

现在 ToDoItem.vue 应该是这样：

```html
<template>
  <div>
    <input type="checkbox" id="todo-item" checked="false" />
    <label for="todo-item">我的待做事项</label>
  </div>
</template>

<script>
  export default {
    props: {
      label: { required: true, type: String },
      done: { default: false, type: Boolean }
    }
  };
</script>
```


通过在组件对象中定义这些道具，我们现在可以在模板中使用这些变量值。让我们从将labelprop添加到组件模板开始。

在 ToDoItem.vue 中的"template"，用{{label}}替换"label"元素的内容，即将原本的：
```html
<label for="todo-item">我的待做事项</label>
```

改为：

```html
<label for="todo-item">{{label}}</label>
```

由于我们将标记label为必需的道具，但我们从未提供该prop的默认值，因此在调用它时，需要将其传递给组件。

在App.vue 文件内部，向"to-do-item""to-do-item"组件添加一个label prop ，就像常规的HTML属性一样：

```html
<to-do-item label="完成移动互联应用大作业"></to-do-item>
```
此时我们可以看到，通过label属性我们将字符串传到了ToDoItem组件：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126201020316.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)
## 6.4 Vue的数据对象：
现在我们有一个带有可更新标签的复选框。但是，我们目前对“ done” prop做不了任何事情——尽管我们可以在UI中选中复选框，但是在应用程序的任何地方都没有记录待办事项是否确实完成。

为此，我们希望将组件的done prop绑定到"input"元素上的checked属性，以便它可以用作是否选中该复选框的记录。但是，在VUE中，prop必须作为一种单向数据绑定，即组件绝不能改变其自身prop的值。

要解决此问题，我们可以使用Vue的data属性来管理done状态。该data属性是我们可以在组件中管理本地状态的地方，它与props属性一起位于组件对象内部，并具有以下结构：

```html
data() {
  return {
    key: value
  }
}
```
我们可以注意到该data属性是一个函数。这是为了在运行时使每个组件实例的数据值保持唯一性，即为每个组件实例分别调用该函数。如果将数据声明为仅一个对象，则该组件的所有实例将会共享相同的值，而这往往是我们不想要的。

我们可以使用this从内部数据访问组件的prop和其他属性。

因此，让我们向ToDoItem组件添加一个data属性。这将返回一个包含单个属性的对象，我们将其称为isDone，其值为this.done。

现在 ToDoItem.vue 应该是这样：

```html
<template>
  <div>
    <input type="checkbox" id="todo-item" checked="false" />
    <label for="todo-item">{{ label }}</label>
  </div>
</template>

<script>
export default {
  props: {
    label: { required: true, type: String },
    done: { default: false, type: Boolean },
  },
  data() {
    return {
      isDone: this.done,
    };
  },
};
</script>
```
Vue在这里做了一点处理——它将我们所有的props直接绑定到该组件实例，因此我们不必调用this.props.done。这就是为什么我们将data属性称为isDone而不是的原因done（即如果都称之为done，在其他组件中将无法区分）。

因此，现在我们需要将该isDone属性附加到组件。与Vue使用{{}}表达式在模板内显示JavaScript表达式的方式类似，Vue具有特殊的语法将JavaScript表达式绑定到HTML元素和组件：v-bind。该v-bind表达式如下所示：

```html
v-bind:attribute="expression"
```

换句话说，我们要为要绑定的任何属性/属性加上前缀v-bind:。在大多数情况下，我们可以使用该v-bind属性的简写，即在属性/prop前面加上一个冒号。因此 :attribute="expression" 与 v-bind:attribute="expression" 相同。

因此，对于我们ToDoItem组件中的复选框，我们可以使用v-bind将isDone属性映射到<input>元素上的checked属性。以下两项是等效的：

```html
<input type="checkbox" id="todo-item" v-bind:checked="isDone" />

<input type="checkbox" id="todo-item" :checked="isDone" />
```
现在我们更新 APP.vue ，在"input"元素中替换 checked="false" 为 :checked="isDone"：

```html
<input type="checkbox" id="todo-item" :checked="isDone" />
```

现在 App.vue 应该是这样：

```html
<template>
  <div id="app">
  <h1>备忘录</h1>
  <ul>
    <li>
      <to-do-item label="完成移动互联应用大作业" :done="false"></to-do-item>
    </li>
  </ul>
</div>
</template>


<script>
import ToDoItem from "./components/ToDoItem.vue";
export default {
  name: "App",
  components: {
    ToDoItem,
  },
};
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
</style>

```

此时我们看到网页待做事项默认变为未完成：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126203038565.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)
## 6.5 给Todos一个唯一的ID：
我们目前只能ToDoList在页面上添加一个组件，因为组件id是硬编码的，而这将导致辅助技术出现错误，因为id需要将标签正确映射到其复选框。

要解决此问题，我们可以通过编程方式在组件数据中进行设置id。

我们可以使用lodash包的uniqueid()方法来帮助保持索引唯一。该软件包导出一个函数，该函数接受一个字符串，并将一个唯一的整数附加到前缀的末尾，从而保持组件id的唯一性。

让我们使用npm将软件包添加到我们的项目中。

首先停止服务器，然后在终端中输入以下命令：

```bash
npm install --save lodash.uniqueid
```

注意该包是安装到项目目录，新项目需要重新安装。

现在，我们可以将该包导入到我们的ToDoItem组件中。在ToDoItem.vue的"script"元素顶部添加：

```html
import uniqueId from 'lodash.uniqueid';
```

接下来，在我们的data属性中添加一个id字段：

```html
data() {
    return {
      isDone: this.done,
      id: uniqueId('todo-')
    };
  }
```
其中 uniqueId() 返回指定的前缀— 'todo-' —并附加一个唯一的字符串。

接下来，将id绑定到我们复选框的id属性和标签的for属性，更新现有id属性和for属性：

```html
<template>
  <div>
    <input type="checkbox" :id="id" :checked="isDone" />
    <label :for="id">{{label}}</label>
  </div>
</template>
```

现在 ToDoItem.vue 应该是这样：

```html
<template>
  <div>
    <input type="checkbox" :id="id" :checked="isDone" />
    <label :for="id">{{label}}</label>
  </div>
</template>

<script>
import uniqueId from 'lodash.uniqueid';
export default {
  props: {
    label: { required: true, type: String },
    done: { default: false, type: Boolean }
  },
  data() {
    return {
      isDone: this.done,
      id: uniqueId('todo-')
    };
  }
};
</script>
```

# 7. 添加待做事项列表：
我们接下来添加更多的 ToDoItem 组件到我们的App。该部分中我们会添加一系列待办事项到App.vue组件，并使用v-for指令遍历这些函数，将它们的每一项展示在ToDoItem组件中。

## 7.1 利用v-for指令渲染列表：
一个有效的待办事项列表需要有多个被渲染的待办事项，Vue中的v-for 可以实现这种效果。它是Vue自带的指令，用于在模板中实现循环，我们可以利用它我们将利用其迭代待办事项列表，将其中的每一项展示为单独的ToDoItem组件。

首先我们需要准备一个待办​​事项清单。添加 data 属性到 App.vue组件对象中，它包含一个 ToDoItems细分，其值是待办事项清单。在最终完成添加新的待办事项功能之前，我们可以先添加一些待办项目，每个待办项目可以用一个对象表示，这个对象包含 name 和 done 属性：

```html
export default {
  name: 'app',
  components: {
    ToDoItem
  },
  data() {
    return {
      ToDoItems: [
        { label: '完成移动互联应用大作业', done: false },
        { label: '复习软件工程第九章', done: false },
        { label: '快乐五排上分', done: true },
        { label: '早睡早起身体倍棒', done: false }
      ]
    };
  }
};
```

现在我们有了一个列表，用可以v-for去展示它们了指令的作用英文方式状语从句：元素的属性类似，就V-的而言，它类似JS中的。for...in循环，v-for="item in items" ——iterms是你要迭代的列表， item 是数组中当前元素的引用。

在进行数据传递之前，我们要了解下一个key属性，它和v-for使用，以帮助Vue标识列表中的元素，这样Vue不需要在列表变化时重新创建它们。

但是Vue需要一个唯一的标识，我们可以使用 lodash.uniqueid() 来实现：
1. 导入 lodash.uniqueid 到 App 组件：
	

	```html
	import uniqueId from 'lodash.uniqueid';
	```
		
2. 添加 id 细分到细分 ToDoItems的每一个元素中，并且将他们赋值为 uniqueId('todo-')，例如：
	

	```html
	{ id: uniqueId('todo-'), label: '早睡早起身体倍棒', done: false },
	```

3. 添加 v-for指令和 key属性到 "li" 元素：
	
	```html
	<ul>
	  <li v-for="item in ToDoItems" :key="item.id">
	    <to-do-item :label="item.label" :done="item.done"></to-do-item>
	  </li>
	</ul>
	```

现在当我们去看运行着的app时，我们会发现待办事项显示了它们自己正确的名字和属性：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126204755982.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)
## 7.2 重构id属性：
因为我们已经要为每一个待办事项创建一个唯一id，所以不妨碍把id作为ToDoItem的一个prop，而无需在每个checkbox里生成它：
1. 添加一个新的propid 到 ToDoItem组件。
2. 标记它为必需，类型是 String 。
3. 为防止命名冲突，删除掉data属性中的id分支。
4. 删除掉 import uniqueId from 'lodash.uniqueid'; 这行。

现在 ToDoItem.vue 应该是这样：

```html
<template>
  <div>
    <input type="checkbox" :id="id" :checked="isDone" />
    <label :for="id">{{ label }}</label>
  </div>
</template>

<script>
export default {
  props: {
    label: { required: true, type: String },
    done: { default: false, type: Boolean },
    id: { required: true, type: String },
  },
  data() {
    return {
      isDone: this.done,
    };
  },
};
</script>
```

渲染后的站点看起来是没有变化的，但是这次重组尝试item.id像其他参数一样，作为prop从App.vue传递给ToDoItem，从而使得代码变得逻辑性一致。

# 8. 添加输入框：
## 8.1 渲染输入框：
接下来我们真正需要的是允许我们的用户在应用程序中输入自己的待办事项的功能，为此，我们需要一个text "input"，一个在提交数据时触发的事件，一个在提交时触发的方法以添加数据并重新呈现列表，以及控制数据的模型。

让我们新建一个组件来允许我们添加新的待办项。

在components目录下，新建文件 ToDoForm.vue：

```html
<template></template>

<script>
  export default {};
</script>
```

然后新建一个HTML表单来允许我们输入新的待办项并把它提交到app。我们需要一个 "form" ，它里面包含一个 "label"，一个 "input"，一个 "button"。更新后的模版如下：

```html
<template>
  <form>
    <label for="new-todo-input">
      还有什么要做的？
    </label>
    <p></p>
    <input
      type="text"
      id="new-todo-input"
      name="new-todo"
      autocomplete="off"
    />
    <button type="submit">
      添加
    </button>
  </form>
</template>
```

现在我们有一个可以form组件可以用来输入新的待办项的标题，它最终会渲染成ToDoItem的标签。

我们把这个组件添加到app中。

返回 App.vue 然后在 "script" 添加以下的语句：

```html
import ToDoForm from './components/ToDoForm';
```

在App组件中注册它：

```html
components: {
    ToDoItem,
    ToDoForm,
  },
```
最后将 ToDoForm组件添加到App中的"template" 中，像下面这样：

```html
<template>
  <div id="app">
    <h1>备忘录</h1>
    <to-do-form></to-do-form>
    <ul>
      <li v-for="item in ToDoItems" :key="item.id">
        <to-do-item :label="item.label" :done="item.done" :id="item.id"></to-do-item>
      </li>
    </ul>
  </div>
</template>
```
现在，当我们查看运行中的站点时，应该会看到显示的新表单：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126210022825.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)
如果我们填写表格并单击“添加”按钮，页面将把表格发回到服务器上，但这并不是我们真正想要的。

我们实际上想要做的是在submit事件上运行一个方法，该方法会将新的待办事项添加到ToDoItem内部定义的数据列表中App。为此，我们需要向组件实例添加一个方法。

## 8.2 使用v-on创建方法并将其绑定到事件：
为了提供给ToDoForm组件一个方法，我们需要将它添加到组件对象，这是一个内部完成methods属性作为我们的组件。

在此组件中，我们需要在组件对象内的属性中添加一个onSubmit()方法。我们将使用它来处理Submit操作：

```html
<script>
export default {
   methods: {
       onSubmit() {
          console.log('form submitted')
       }
   }
}
</script>
```
接下来，我们需要将方法绑定到"form"元素的submit事件处理程序上。

就像Vue如何使用v-bind语法来绑定属性一样，Vue有一个特殊的指令用于事件处理：v-on。该v-on指令通过v-on:event="method"语法起作用。就像v-bind，还有一种简写语法：@event="method"。

然后将submit处理程序添加到"form"元素中，如下所示：

```html
<form @submit="onSubmit">
```

为了防止浏览器发布到服务器，我们需要停止事件在页面中冒泡的默认操作。Vue具有一种特殊的语法，称为事件修饰符，可以在模板中为我们处理此事件。

修饰符会附加到事件的末尾，并带有一个点，如下所示：@event.modifier。以下事件修饰符的列表：

- .stop：阻止事件传播。等效Event.stopPropagation()于常规JavaScript事件。
- .prevent：防止事件的默认行为。等同于Event.preventDefault()。
- .self：仅当事件是从此确切元素调度的时才触发处理程序。
- {.key}：仅通过指定的键触发事件处理程序。MDN包含有效键值的列表；多字键只需要转换为kebab大小写即可（例如page-down）。
- .native：在组件的根（最外面的包装）元素上侦听本地事件。
- .once：监听事件，直到事件被触发一次，然后不再触发。
- .left：仅通过鼠标左键事件触发处理程序。
- .right：仅通过鼠标右键事件触发处理程序。
- .middle：仅通过鼠标中键事件触发处理程序。
- .passive：等效于在使用的{ passive: true }JavaScript中创建事件监听器时使用参数addEventListener()。

在这种情况下，我们需要使用.prevent处理程序来停止浏览器的默认提交动作：

```html
<form @submit.prevent="onSubmit">
```

表示再点击提交按钮时，阻止事件传播，并激活onSubmit函数。

此时点击【提交】可以看到控制台有相应的输出，并且网页不再刷新：

![在这里插入图片描述](https://img-blog.csdnimg.cn/2021012621085331.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)
接下来，我们需要一种从表单中获取值的方法，以便"input"可以将新的待办事项添加到ToDoItems数据列表中。

## 8.3 从表单中获取指定值：
我们需要的第一件事是通过表单中的data属性来跟踪待办事项的值。

data()向我们的ToDoForm组件对象添加一个返回label字段的方法。我们可以将的初始值设置为label空字符串：

```html
<script>
export default {
  methods: {
    onSubmit() {
      console.log("form submitted");
    },
  },
  data() {
    return {
      label: "",
    };
  },
};
</script>
```

现在，我们需要某种方式将 "input" 字段的值附加到该label字段。Vue为此有一个特殊的指令：v-model。v-model绑定到您在其上设置的data属性，并使它与"input"保持同步。v-model适用于所有各种输入类型，包括复选框，单选按钮和选择输入。为了使用v-model，我们向"input"中添加v-model="variable"的结构属性：

```html
<input
  type="text"
  id="new-todo-input"
  name="new-todo"
  autocomplete="off"
  v-model="label" />
```

让我们在onSubmit()方法中来测试一下提交的数据的值。在组件中，使用this关键字访问数据属性。因此，我们label使用来访问我们的字段this.label：

```html
methods: {
    onSubmit() {
      console.log("Label value: ", this.label);
    },
  },
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126211909695.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)
可以看到我们的 label 值已经和输入框的内容同步。

## 8.4 使用修饰符更改v-model的行为：
与事件修饰符类似，我们还可以添加修饰符来更改v-model的行为。就我们而言，有两个值得考虑的问题。第一个，.trim将从输入之前或之后删除空格。我们可以修改添加到我们的v-model语句，像这样：

```html
v-model.trim="label"
```

我们应该考虑的第二个修饰符称为.lazy。v-model同步文本输入的值时，此修饰符会更改。如前所述，v-model同步通过使用事件更新变量来进行。对于文本输入，此同步是使用inputevent发生的。通常，这意味着Vue在每次击键后都会同步数据。该.lazy修改将导致v-model使用该change事件来代替。这意味着Vue仅在输入失去焦点或提交表单时才同步数据。对我们而言这是更合理的，因为我们只需要最终数据。

要同时使用.lazy修饰符和.trim修饰符，可以将它们链接起来，例如：

```html
v-model.lazy.trim="label"
```

此时我们将 "input" 修改为：

```html
<input
      type="text"
      id="new-todo-input"
      name="new-todo"
      autocomplete="off"
      v-model.lazy.trim="label"
    />
```

## 8.5 通过自定义事件将数据传递给父组件：
现在我们需要做的下一件事是将新创建的待办事项传递给我们的App组件。为此，我们可以让ToDoForm发出一个自定义事件来传递数据，并使用App监听它。这与HTML元素上的事件非常相似：子组件可以发出可通过v-on监听的事件。


在ToDoFormon的Submit事件下，让我们添加一个todo-added事件。自定义事件的发出方式如下：

```html
this.$emit("event-name")
```

因此我们替换在onSubmit()里面的console.log()为：

```html
this.$emit("todo-added");
```
然后向App.vue添加一个methods属性addToDo()，如下所示：

```html
export default {
  name: "app",
  components: {
    ToDoItem,
    ToDoForm,
  },
  data() {
    return {
      ToDoItems: [
        { id: uniqueId("todo-"), label: "完成移动互联应用大作业", done: false },
        { id: uniqueId("todo-"), label: "复习软件工程第九章", done: false },
        { id: uniqueId("todo-"), label: "快乐五排上分", done: true },
        { id: uniqueId("todo-"), label: "早睡早起身体倍棒", done: false },
      ],
    };
  },
  methods: {
    addToDo() {
      console.log("添加成功");
    },
  },
};
```

接下来，将事件todo-added的监听器添加到"to-do-form""/to-do-form"中，事件触发时将调用addToDo()方法。使用@简写，监听器将如下所示：

```html
@todo-added="addToDo"
```

因此我们将其修改为：

```html
<to-do-form @todo-added="addToDo"></to-do-form>
```
表示在监听到 todo-added 事件时，调用addToDo()方法：
![在这里插入图片描述](https://img-blog.csdnimg.cn/202101262143375.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)

但是现在我们仍然没有将任何数据传递回App.vue组件。

我们可以通过this.$emit()向ToDoForm组件中的函数传递其他参数来实现。

在这种情况下，当我们触发事件时，我们希望将label数据与之一起传递。这是通过将要传递的数据作为另一个参数包含在$emit()方法中来完成的，可以通过如下方法实现：

```html
this.$emit("todo-added", this.label)
```

这类似于JavaScript事件包含数据的方式，除了自定义Vue事件默认情况下不包含任何事件对象。这意味着发出的事件将直接匹配我们提交的任何对象。在本例中，我们的事件对象将只是一个字符串。

因此我们修改onSubmit函数：

```html
onSubmit() {
  this.$emit('todo-added', this.label)
}
```

然后向我们的addToDo()方法中添加一个包含label新待办事项的参数：

```html
methods: {
  addToDo(toDoLabel) {
    console.log('To-do added:', toDoLabel);
  }
}
```
可以看到输入的字符串作为参数，传递到了addToDo中：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126215034272.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)

## 8.6 将新的待办事项添加到我们的数据中：
现在我们有了App.vue中ToDoForm的可用数据，我们需要将一个代表它的项目添加到ToDoItems数组中。这可以通过将新的待办事项对象推入包含我们的新数据的数组来完成。

首先重写addToDo()方法：

```html
addToDo(toDoLabel) {
  this.ToDoItems.push({id:uniqueId('todo-'), label: toDoLabel, done: false});
}
```

这会将 {id:uniqueId('todo-'), label: toDoLabel, done: false} 推送到数据列表中：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126215618892.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)

在继续之前，让我们做进一步的改进。如果在输入为空时提交表单，则没有文本的待办事项仍会添加到列表中。为了解决这个问题，我们可以防止在名称为空时触发添加todo的事件。由于名称已被.trim伪指令修剪，因此我们只需要测试空字符串即可：

回到ToDoForm组件，并更新onSubmit()：

```html
onSubmit() {
      if (this.label === "") {
        return;
      }
      this.$emit("todo-added", this.label);
    },
```

现在我们将无法将空项目添加到待办事项列表。

## 8.7 使用v-model更新的输入值：
我们的ToDoForm组件中还有另一件事需要修复——提交后，"input"仍然包含旧值。但这很容易解决——因为我们v-model用来将数据绑定到"input"in ToDoForm，如果我们将name参数设置为等于空字符串，那么输入也会更新。

```html
onSubmit() {
  if(this.label === "") {
    return;
  }
  this.$emit('todo-added', this.label);
  this.label = "";
}
```
# 9. 使用CSS样式化Vue组件：
Vue具有三种样式化应用程序的方法：

1. 外部CSS文件。
2. 单个文件组件（.vue文件）中的全局样式。
3. 单个文件组件中组件范围的样式。

## 9.1 外部CSS文件的样式：
在src/assets目录中创建一个名为的reset.css文件：

```css
/*reset.css*/
/* RESETS */
*,
*::before,
*::after {
  box-sizing: border-box;
}
*:focus {
  outline: 3px dashed #228bec;
}
html {
  font: 62.5% / 1.15 sans-serif;
}
h1,
h2 {
  margin-bottom: 0;
}
ul {
  list-style: none;
  padding: 0;
}
button {
  border: none;
  margin: 0;
  padding: 0;
  width: auto;
  overflow: visible;
  background: transparent;
  color: inherit;
  font: inherit;
  line-height: normal;
  -webkit-font-smoothing: inherit;
  -moz-osx-font-smoothing: inherit;
  -webkit-appearance: none;
}
button::-moz-focus-inner {
  border: 0;
}
button,
input,
optgroup,
select,
textarea {
  font-family: inherit;
  font-size: 100%;
  line-height: 1.15;
  margin: 0;
}
button,
input {
  /* 1 */
  overflow: visible;
}
input[type="text"] {
  border-radius: 0;
}
body {
  width: 100%;
  max-width: 68rem;
  margin: 0 auto;
  font: 1.6rem/1.25 "Helvetica Neue", Helvetica, Arial, sans-serif;
  background-color: #f5f5f5;
  color: #4d4d4d;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
}
@media screen and (min-width: 620px) {
  body {
    font-size: 1.9rem;
    line-height: 1.31579;
  }
}
/*END RESETS*/
```
然后在src/main.js文件中，如下导入reset.css文件：

```javascript
import './assets/reset.css';
```

重置后的样式：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126220827130.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)
## 9.2 向单个文件组件添加全局样式：
我们也可以直接将它们添加到的"style"标签中，例如修改App.vue：

```css
<style>
/* Global styles */
.btn {
  padding: 0.8rem 1rem 0.7rem;
  border: 0.2rem solid #4d4d4d;
  cursor: pointer;
  text-transform: capitalize;
}
.btn__danger {
  color: #fff;
  background-color: #ca3c3c;
  border-color: #bd2130;
}
.btn__filter {
  border-color: lightgrey;
}
.btn__danger:focus {
  outline-color: #c82333;
}
.btn__primary {
  color: #fff;
  background-color: #000;
}
.btn-group {
  display: flex;
  justify-content: space-between;
}
.btn-group > * {
  flex: 1 1 auto;
}
.btn-group > * + * {
  margin-left: 0.8rem;
}
.label-wrapper {
  margin: 0;
  flex: 0 0 100%;
  text-align: center;
}
[class*="__lg"] {
  display: inline-block;
  width: 100%;
  font-size: 1.9rem;
}
[class*="__lg"]:not(:last-child) {
  margin-bottom: 1rem;
}
@media screen and (min-width: 620px) {
  [class*="__lg"] {
    font-size: 2.4rem;
  }
}
.visually-hidden {
  position: absolute;
  height: 1px;
  width: 1px;
  overflow: hidden;
  clip: rect(1px 1px 1px 1px);
  clip: rect(1px, 1px, 1px, 1px);
  clip-path: rect(1px, 1px, 1px, 1px);
  white-space: nowrap;
}
[class*="stack"] > * {
  margin-top: 0;
  margin-bottom: 0;
}
.stack-small > * + * {
  margin-top: 1.25rem;
}
.stack-large > * + * {
  margin-top: 2.5rem;
}
@media screen and (min-width: 550px) {
  .stack-small > * + * {
    margin-top: 1.4rem;
  }
  .stack-large > * + * {
    margin-top: 2.8rem;
  }
}
/* End global styles */
#app {
  background: #fff;
  margin: 2rem 0 4rem 0;
  padding: 1rem;
  padding-top: 0;
  position: relative;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2), 0 2.5rem 5rem 0 rgba(0, 0, 0, 0.1);
}
@media screen and (min-width: 550px) {
  #app {
    padding: 4rem;
  }
}
#app > * {
  max-width: 50rem;
  margin-left: auto;
  margin-right: auto;
}
#app > form {
  max-width: 100%;
}
#app h1 {
  display: block;
  min-width: 100%;
  width: 100%;
  text-align: center;
  margin: 0;
  margin-bottom: 1rem;
}
</style>
```
效果如图：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126221035247.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)

## 9.3 在Vue中添加CSS类：
我们应该应用按钮CSS类到"button"我们的ToDoForm组件。由于Vue模板是有效的HTML，因此可以通过在class=""元素中添加属性，以与纯HTML相同的方式进行操作。

比如：

```html
<button type="submit" class="btn btn__primary btn__lg">
  添加
</button>
```
和

```html
<label for="new-todo-input" class="label__lg">
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126221309652.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)
现在 ToDoItem.vue 应该是这样：

```html
<template>
  <form @submit.prevent="onSubmit">
    <h2 class="label-wrapper">
      <label for="new-todo-input" class="label__lg">
        还有什么要做的？
      </label>
    </h2>
    <input
      type="text"
      id="new-todo-input"
      name="new-todo"
      autocomplete="off"
      v-model.lazy.trim="label"
      class="input__lg"
    />
    <button type="submit" class="btn btn__primary btn__lg">
      添加
    </button>
  </form>
</template>

<script>
export default {
  methods: {
    onSubmit() {
      if (this.label === "") {
        return;
      }
      this.$emit("todo-added", this.label);
      this.label = "";
    },
  },
  data() {
    return {
      label: "",
    };
  },
};
</script>
```

同时可以添加：

```html
<ul aria-labelledby="list-summary" class="stack-large">
```

来帮助调整间距：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126221447782.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)
# 10. computed属性-添加统计功能：
在本节我们将使用Vue称为计算属性的功能添加一个计数器，以显示已完成的待办事项的数量。

## 10.1 添加汇总计数器：

要创建计算属性，我们需要向组件对象添加一个computed属性，就像我们之前使用的methods属性一样。

将以下代码添加到App组件对象下方的methods属性。listSummary 方法将获取标记为完成状态的ToDoItems数量，并返回报告此内容的字符串：

```html
computed: {
    listSummary() {
      const numberFinishedItems = this.ToDoItems.filter((item) => item.done)
        .length;
      return `已完成：${numberFinishedItems} 未完成：${
        this.ToDoItems.length - numberFinishedItems
      }`;
    },
  },
```
现在我们可以将{{listSummary}}直接添加到模板中：

```html
<h2 id="list-summary">{{listSummary}}</h2>
<ul aria-labelledby="list-summary" class="stack-large">
  <li v-for="item in ToDoItems" :key="item.id">
    <to-do-item :label="item.label" :done="item.done" :id="item.id"></to-do-item>
  </li>
</ul>
```

## 10.2 跟踪“完成”状态的更改：

我们可以使用事件来捕获复选框更新并相应地管理我们的列表。

由于我们不依靠按钮来触发更改，因此我们可以将@change事件处理程序附加到每个复选框，而不必使用v-model。

更新 ToDoItem.vue 中的"input"元素：

```html
<input type="checkbox" class="checkbox" :id="id" :checked="isDone"
       @change="$emit('checkbox-changed')" />
```
然后在 App.vue 中，的addToDo()方法下方添加一个名为updateDoneStatus()的新方法。此方法应采用一个参数：待办事项ID。

我们要查找 App.vue 的数据列表中具有匹配项的项目id并将其done状态更新为与其当前状态相反的状态：

```html
updateDoneStatus(toDoId) {
      const toDoToUpdate = this.ToDoItems.find((item) => item.id === toDoId);
      toDoToUpdate.done = !toDoToUpdate.done;
    },
```

因此我们希望每当一个 ToDoItem 发出checkbox-changed事件时，都运行此方法，并将其item.id作为参数传递：

```html
<to-do-item :label="item.label" :done="item.done" :id="item.id"
            @checkbox-changed="updateDoneStatus(item.id)">
</to-do-item>
```

这样我们就实现了动态计数：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210127081136278.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)

# 11. Vue条件渲染-编辑现有待办事项：
现在是时候添加我们仍然缺少的功能的主要部分之一了，即编辑现有待办事项的功能。为此，我们将利用Vue的条件渲染功能（即v-if和v-else），使我们能够在现有待办事项视图和可更新待办事项标签的编辑视图之间切换。我们还将研究添加功能以删除待办事项。

## 11.1 创建一个编辑组件：
我们可以先创建一个单独的组件来处理编辑功能。在components目录中，创建一个名为ToDoItemEditForm.vue的新文件：

```html
<template>
  <form class="stack-small" @submit.prevent="onSubmit">
    <div>
      <label class="edit-label">编辑事项 &quot;{{label}}&quot;</label>
      <input :id="id" type="text" autocomplete="off" v-model.lazy.trim="newLabel" />
    </div>
    <div class="btn-group">
      <button type="button" class="btn" @click="onCancel">
        取消
        <span class="visually-hidden">editing {{label}}</span>
      </button>
      <button type="submit" class="btn btn__primary">
        保存
        <span class="visually-hidden">edit for {{label}}</span>
      </button>
    </div>
  </form>
</template>
<script>
export default {
  props: {
    label: {
      type: String,
      required: true
    },
    id: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      newLabel: this.label
    };
  },
  methods: {
    onSubmit() {
      if (this.newLabel && this.newLabel !== this.label) {
        this.$emit("item-edited", this.newLabel);
      }
    },
    onCancel() {
      this.$emit("edit-cancelled");
    }
  }
};
</script>
<style scoped>
.edit-label {
  font-family: Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #0b0c0c;
  display: block;
  margin-bottom: 5px;
}
input {
  display: inline-block;
  margin-top: 0.4rem;
  width: 100%;
  min-height: 4.4rem;
  padding: 0.4rem 0.8rem;
  border: 2px solid #565656;
}
form {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}
form > * {
  flex: 0 0 100%;
}
</style>
```

在上面的代码中，我们创建一个带有用于编辑待办事项名称的字段的"input"表单，以及一个“保存”按钮和一个“取消”按钮：
1. 单击“保存”按钮后，组件将通过item-edited事件发出新标签。
2. 单击“取消”按钮时，组件通过发出edit-cancelled事件来发出信号。

## 11.2 修改我们的ToDoItem组件：
我们需要在 ToDoItem 中添加一个变量来跟踪项目是否正在被编辑，以及一个按钮来切换该变量。我们还将添加一个 Delete 按钮来删除待办事项：

```html
<template>
  <div class="stack-small">
    <div class="custom-checkbox">
      <input type="checkbox" class="checkbox" :id="id" :checked="isDone"
             @change="$emit('checkbox-changed')" />
      <label :for="id" class="checkbox-label">{{label}}</label>
    </div>
    <div class="btn-group">
      <button type="button" class="btn"  @click="toggleToItemEditForm">
        编辑 <span class="visually-hidden">{{label}}</span>
      </button>
      <button type="button" class="btn btn__danger" @click="deleteToDo">
        删除 <span class="visually-hidden">{{label}}</span>
      </button>
    </div>
  </div>
</template>
```

效果如图：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210127082253476.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)
为了布局目的，我们在整个模板周围添加了包装器 "div"，并且我们还添加了“编辑”和“删除”按钮：

1. 单击“编辑”按钮时，将切换显示ToDoItemEditForm组件，以便我们可以通过名为toggleToItemEditForm()的事件处理函数使用它来编辑待办事项。该处理程序将isEditing标志设置为true。
2. 单击“删除”按钮后，将通过名为deleteToDo()的事件处理函数删除待办事项。在此处理程序中，我们将向我们的父组件发出一个item-deleted事件，以便可以更新列表。

然后让我们定义单击处理程序和必要的isEditing标志：

```html
data() {
  return {
    isDone: this.done,
    isEditing: false
  };
}
```

然后将以下方法添加到data()属性下面的method属性中：

```html
methods: {
    deleteToDo() {
      this.$emit('item-deleted');
    },
    toggleToItemEditForm() {
      this.isEditing = true;
    }
  }
```
## 11.3 通过v:if和v:else有条件地显示组件：
现在我们有了一个isEditing标志，可以用来表示该项目正在被编辑（或未被编辑）。如果isEditing为true，则我们要使用该标志ToDoItemEditForm而不是复选框来显示我们的标志。为此，我们将使用另一个Vue指令：v-if。

该v-if指令仅在传递给它的值是真实的时才渲染一个块。这类似于if语句在JavaScript中的工作方式。v-if还具有相应的v-else-if和v-else指令，以提供Vue模板中等效的JavaScriptelse if和else逻辑。

首先将v-if="!isEditing"添加到ToDoItem组件的根目录"div"中：

```html
<div class="stack-small" v-if="!isEditing">
```
然后在该<div>结束标记下添加以下行：

```html
<to-do-item-edit-form v-else :id="id" :label="label"></to-do-item-edit-form>
```
我们还需要导入和注册ToDoItemEditForm组件：

```html
import ToDoItemEditForm from "./ToDoItemEditForm";
```

```html
components: {
  ToDoItemEditForm
},
```
这样的话就实现了两个组件的条件显示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210127083359580.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)
## 11.4 退出编辑模式：
但是目前没有退回的方法。为了解决这个问题，我们需要向组件中添加更多事件处理程序。

首先，我们需要在ToDoItem组件的methods中添加一个itemEdited()方法。此方法应将新的事项标签作为参数，向父组件发出itemEdited事件，并isEditing设置为false：

```html
itemEdited(newLabel) {
  this.$emit('item-edited', newLabel);
  this.isEditing = false;
}
```

然后我们添加 editCancelled() 方法，这个方法不带参数，只是将isEditing设为false。将这个方法添加到前一个方法的下面：

```html
editCancelled() {
  this.isEditing = false;
}
```

最后我们将为ToDoItemEditForm组件发出的事件添加事件处理程序，并将适当的方法附加到每个事件：

```html
<to-do-item-edit-form
    v-else
    :id="id"
    :label="label"
    @item-edited="itemEdited"
    @edit-cancelled="editCancelled"
  >
  </to-do-item-edit-form>
```
这样我们就可以在编辑表单和复选框之间切换了。

## 11.5 更新和删除待办事项：
现在我们可以在编辑表单和复选框之间切换。但是，我们实际上尚未处理过将ToDoItems类别更新回App.vue的过程。要解决此问题，我们需要监听item-edited事件，并相应地更新列表。我们还将要处理delete事件，以便我们可以删除待办事项。

在App.vue的methods属性内现有方法的下面，将以下新方法添加到组件对象中：

```html
deleteToDo(toDoId) {
  const itemIndex = this.ToDoItems.findIndex(item => item.id === toDoId);
  this.ToDoItems.splice(itemIndex, 1);
},
editToDo(toDoId, newLabel) {
  const toDoToEdit = this.ToDoItems.find(item => item.id === toDoId);
  toDoToEdit.label = newLabel;
}
```
接下来，我们将为item-deleted和item-edited事件添加事件监听器：

```html
<to-do-item :label="item.label" :done="item.done" :id="item.id"
            @checkbox-changed="updateDoneStatus(item.id)"
            @item-deleted="deleteToDo(item.id)"
            @item-edited="editToDo(item.id, $event)">
</to-do-item>
```

$event变量是一个特殊的Vue变量，用于将事件数据传递给方法。使用本地HTML事件（如click）时，这会将本地事件对象传递给您的方法。

现在就可以编辑、保存和删除了：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210127084257736.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210127084306576.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)
## 11.6 修复isDone状态的小错误：
但是实际上我们遗留了一个小 bug。比如我们尝试这样做：

1. 选中（或取消选中）一个待办事项复选框。
2. 按下该待办事项的“编辑”按钮。
3. 按下“取消”按钮取消编辑。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210127084610951.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)
我们会发现计数器不能正确显示。这是因为在 data 属性内的 isDone 只在组件加载时给出 this.done 的值。

首先我们删除：

```html
isDone: this.done,
```
然后添加：

```html
computed: {
  isDone() {
    return this.done;
  }
},
```

现在，当我们保存并重新加载时，我们会发现问题已解决——在待办事项模板之间切换时，复选框状态现在得以保留：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210127085712828.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)
# 关注我的公众号：
感兴趣的同学关注我的公众号——可达鸭的深度学习教程：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210127153004430.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)
