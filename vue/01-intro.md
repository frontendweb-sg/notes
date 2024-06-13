# What is virtual dom?

A way of representing the `actual dom` with `javascript` `object`.

`Example:`

```html
<div>Hello World</div>
```

Convert into virtual node `VNode`

```js
{
    tag:'div',
    children: [
        {
            text:'Hello world'
        }
    ]
}

// Look it is simpley a javascript object.
```

Vue takes this `VNode` and `mounted` on the `dom` which update we see in the `browser`.

`Render` function return virtual dom nodes.

```
<div>Hello world</div> -> Render function -> create VNode -> display on the browser
```

`Example:`

```html
<div>Hello World</div>
```

```js

// render function looks something like this
Render(h){
     return h('div','Hello World')
}
// it generates this vnode
{
    tag:'div',
    children: [
        {
            text:'Hello world'
        }
    ]
}
// when component changes, it update the vnode
Render(h){
     return h('div','Hello World1')
}
{
    tag:'div',
    children: [
        {
            text:'Hello world1'
        }
    ]
}
// then vue finally compare the old vnode and new vnode and updates in the most efficent way.
```
