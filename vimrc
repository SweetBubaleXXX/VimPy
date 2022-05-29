set nocompatible
set ruler
syntax on

set belloff=all

set ignorecase
set smartcase

set tabstop=4
set shiftwidth=4
set softtabstop=4
set expandtab
set smarttab
set smartindent

set mouse=a
set backspace=2

nnoremap <F2> :set invpaste paste?<CR>
set pastetoggle=<F2>
set showmode

nnoremap <F3> :set invhlsearch<CR>

nnoremap <F4> :set number!<CR>

inoremap <C-@> <C-x><C-p>

filetype plugin on
set omnifunc=syntaxcomplete#Complete

set undodir=~/.vim/undo//
set backupdir=~/.vim/backup//
set directory=~/.vim/swp//

set langmap=ФИСВУАПРШОЛДЬТЩЗЙКЫЕГМЦЧНЯ;ABCDEFGHIJKLMNOPQRSTUVWXYZ,фисвуапршолдьтщзйкыегмцчня;abcdefghijklmnopqrstuvwxyz
