filter_chunk <- function(df, pos) {
  df <- suppressMessages(as_tibble(df, .name_repair = 'universal'))
  df <- df %>% 
    filter(Pango.lineage == 'BA.2.86' | Pango.lineage == 'BA.2.86.1') %>%
    mutate(Collection.date = as.Date(Collection.date, format = '%Y-%m-%d'))
}  
