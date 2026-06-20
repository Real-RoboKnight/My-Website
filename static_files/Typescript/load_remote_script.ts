export type LoadScriptOptions = {
    async?: boolean;
    defer?: boolean;
    crossOrigin?: HTMLScriptElement['crossOrigin'];
    referrerPolicy?: HTMLScriptElement['referrerPolicy'];
};

export function loadScriptFromUrl(url: string, options: LoadScriptOptions = {}): Promise<HTMLScriptElement> {
    if (!url) {
        return Promise.reject(new Error('Script URL is required.'));
    }

    const existing = document.querySelector<HTMLScriptElement>(`script[src="${url}"]`);
    if (existing) {
        if (existing.dataset.loaded === 'true') {
            return Promise.resolve(existing);
        }

        return new Promise((resolve, reject) => {
            existing.addEventListener('load', () => resolve(existing), { once: true });
            existing.addEventListener('error', () => reject(new Error(`Failed to load script: ${url}`)), { once: true });
        });
    }

    return new Promise((resolve, reject) => {
        const script = document.createElement('script');
        script.src = url;
        script.async = options.async ?? true;
        script.defer = options.defer ?? true;

        if (options.crossOrigin !== undefined) {
            script.crossOrigin = options.crossOrigin;
        }

        if (options.referrerPolicy !== undefined) {
            script.referrerPolicy = options.referrerPolicy;
        }

        script.addEventListener('load', () => {
            script.dataset.loaded = 'true';
            resolve(script);
        }, { once: true });

        script.addEventListener('error', () => {
            script.remove();
            reject(new Error(`Failed to load script: ${url}`));
        }, { once: true });

        document.head.appendChild(script);
    });
}
