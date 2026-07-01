import Quill from "quill";

/**
 * Used to add a rich text editor to an html form. Add a <div name="stuff"></div> to your form, and this will make it a send html in the form
 * @param id the <div name="stuff"></div> 
 * @param form the form that the data will be sent in
 */
export function rich_text_form(id: HTMLDivElement, form: HTMLFormElement): Quill {
    const toolbarOptions = [
        ['clean', 'bold', 'italic', 'underline', 'blockquote', 'code-block', { 'color': [] }, { 'background': [] }, { 'align': [] },],
        ['link', 'formula', { 'script': 'sub' }, { 'script': 'super' }],
        [{ 'list': 'ordered' }, { 'list': 'bullet' }, { 'indent': '-1' }, { 'indent': '+1' }],

        [{ 'header': [1, 2, 3, false] }, { 'size': ['small', false, 'large', 'huge'] }],

    ];

    const quill = new Quill(id, {
        modules: {
            toolbar: toolbarOptions
        },
        theme: "snow"
    });

    const editorHeight = id.dataset.editorHeight ?? "16rem";
    quill.root.style.minHeight = editorHeight;

    document.querySelectorAll(".ql-toolbar").forEach(function (toolbar) {
        toolbar.querySelectorAll("*").
            forEach(function (item) { item.setAttribute("tabindex", "-1"); });
    })

    const name: string | null = id.getAttribute("name");

    if (name == null) throw "ID must be a div with a name set";

    form.addEventListener('formdata', (event) => {
        event.formData.append(
            name,
            quill.getSemanticHTML()
        )
    })
    return quill
}
