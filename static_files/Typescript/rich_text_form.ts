import Quill from "quill";

/**
 * Used to add a rich text editor to an html form. Add a <div name="stuff"></div> to your form, and this will make it a send html in the form
 * @param id the <div name="stuff"></div> 
 * @param form the form that the data will be sent in
 */
export function make_div_editor_form(id: HTMLDivElement, form: HTMLFormElement) {
    const toolbarOptions = [
        ['bold', 'italic', 'underline'],
        ['blockquote', 'code-block'],
        [{ 'list': 'ordered' }, { 'list': 'bullet' }, { 'list': 'check' }],
        ['link', 'formula', { 'script': 'sub' }, { 'script': 'super' }],
        [{ 'indent': '-1' }, { 'indent': '+1' }],

        [{ 'header': [1, 2, 3, false] }, { 'size': ['small', false, 'large', 'huge'] }, { 'font': [] }, { 'color': [] }, { 'background': [] }],

        [{ 'align': [] }, 'clean'],

    ];

    const quill = new Quill(id, {
        modules: {
            toolbar: toolbarOptions
        },
        theme: "snow"
    });

    const name: string | null = id.getAttribute("name");

    if (name == null) throw "ID must be a div with a name set";

    form.addEventListener('formdata', (event) => {
        event.formData.append(
            name,
            quill.getSemanticHTML()
        )
    })
}
