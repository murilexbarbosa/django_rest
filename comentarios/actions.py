def reprova_comentarios(modeladmin, request, queryset):
    queryset.update(aprovado=False)

def aprova_comentarios(modeladmin, request, queryset):
    queryset.update(aprovado=True)

reprova_comentarios.short_description = 'Reprovar Comentarios'
aprova_comentarios.short_description = 'Aprovar Comentarios'