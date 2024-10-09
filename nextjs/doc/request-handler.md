# What are route handlers?

Route handlers allow you to create custome request handlers for a given route using Web `Request` and `Response` API.

`Note:`

- Route handler are only available inside `app` Directory, they are the equivalent of API Routes inside pages directory.

<br />

**`How to define route handler:`**

You can use `route.js|ts` file inside app directory.

`Example:`

```ts
export const dynamic = "force-dynamic"; // defaults to auto
export async function GET(request: Request) {}
```

`Note:`

- Route Handlers can be nested inside the app directory.
- similar to `page.js` and `layout.js`.
- But there cannot be a `route.js` file at the same route segment level as `page.js`.

**`Supported http method:`**

- GET
- POST
- PUT
- PATCH
- DELETE
- HEAD
- OPTIONS

If an unsupported method is called, Next.js will return a `405 Method Not Allowed response`.

In addition to support native `Request` and `Response`. Next.js extends them with `NextRequest` and `NextResponse` to provide convinient helpers for advanced use cases.

**`Create a post get api`**

```ts
// api/post/route.ts
import { Post } from "models/user";

export async function GET() {
  await connectDb(); // mongodb connection
  const posts = await Post.find(); // Get all post from the database
  return NextResponse.json(posts, { status: 200 });
}
```

**`Caching:`**

Route Handlers are cached by default when using the GET method with the `Response` object.

**`Opting out of caching:`**

You can opt out of caching by:

- Using the `Request` object with `GET` method.

  `Example:`

  ```ts
  // api/post/route.ts
  import { Post } from "models/post";

  export async function GET(req: Request) {
    await connectDb(); // mongodb connection
    const { searchParams } = new URL(req.url);
    const id = searchParams.get("id");
    const posts = await Post.find(); // Get all post from the database
    return NextResponse.json(posts, { status: 200 });
  }

  // Or
  export async function GET(req: NextRequest) {
    await connectDb(); // mongodb connection
    const searchParams = req.nextUrl.searchParams(req.url);
    const query = searchParams.get("query");
    const posts = await Post.find(); // Get all post from the database
    return NextResponse.json(posts, { status: 200 });
  }
  ```

- Using any of the other `HTTP` methods.

  `Example:`

  ```ts
  // api/post/route.ts
  import { Post } from "models/post";

  export async function Post(req: Request) {
    await connectDb(); // mongodb connection
    const body = await req.json();

    const post = await new Post(body);
    const result = await post.save();

    return NextResponse.json(result, { status: 201 });
  }
  ```
