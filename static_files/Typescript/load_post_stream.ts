interface Post {
    slug: string;
    title: string;
    description: string;
    updated_at: string;
}

type Stream = Array<Post>

export function load_post_stream(div: HTMLDivElement, stream: string, start?: number, count?: number) {
    const params = new URLSearchParams();
    if (start)
        params.append("start", start.toString());
    if (count)
        params.append("count", count.toString());

    fetch(`/blog/stream/${stream}?${params}`)
        .then(result => result.json())
        .then((stream: Stream) => {
            stream.forEach(post => {

                const elem = document.createElement("a");
                elem.href = `/blog/post/${post.slug}`;
                elem.className = "text-decoration-none text-reset d-block";
                elem.innerHTML = `
        <div class="card mb-3">
            <div class="card-body py-2">
                <h3 class="card-title mb-1">${post.title}</h3>
                <p class="card-text mb-0">${post.description}</p>
            </div>
        </div>
    `;
                div.appendChild(elem);
            });
        });

}